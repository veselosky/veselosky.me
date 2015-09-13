#!/usr/bin/env python
"""
Markdown to JSON.

Usage:
    md2json.py [--extension=EXT...] <infile> [<outfile>]

Options:
    -x --extension=EXT      A python-markdown extension module to load.

Note: the "markdown.extensions.meta" extension is loaded automatically.
"""
import datetime
import json
import logging
import markdown
import pytz
import sys

from dateutil.parser import parse as parse_date
from docopt import docopt

logging.basicConfig(level=logging.INFO)
zone = pytz.timezone('America/New_York')
default_extensions = [
    'markdown.extensions.meta',
    'markdown.extensions.headerid',
    'pyembed.markdown'
]
arguments = docopt(__doc__)
extensions = set(arguments['--extension'] + default_extensions)


class SmartJSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        else:
            return super(SmartJSONEncoder, self).default(o)

logging.debug("Processing %s" % arguments['<infile>'])

md = markdown.Markdown(extensions=extensions, output_format='html5')
with open(arguments['<infile>']) as infile:
    mtext = infile.read()

html = md.convert(mtext)
metadata = md.Meta
# The metadata needs a lot of clean up, because:
# 1. meta ext reads everything as a list, but most values should be scalar
# 2. because humans are sloppy, we treat keys as case-insensitive
# 3. because humans are sloppy, we parse and normalize date values
metadict = {}
for key, value in metadata.items():
    if key.lower() in ['date', 'published', 'updated']:
        metadict[key.lower()] = zone.localize(parse_date(value[0]))
    else:
        metadict[key.lower()] = value[0] if len(value) == 1 else value
metadict['_content'] = html

if arguments['<outfile>']:
    outfile = open(arguments['<outfile>'], 'w')
    # FIXME this path is relative to the current dir, but SHOULD be
    # realative to siteroot.
    metadict['path'] = arguments['<outfile>']
else:
    outfile = sys.stdout

outfile.write(
    json.dumps(metadict,
               sort_keys=True,
               indent=2,
               cls=SmartJSONEncoder
               ))
