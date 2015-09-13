#!/usr/bin/env python
"""
Jinja2 template renderer.

This script will render a jinja2 template to STDOUT. The template context is
constructed from data files fed to the script.

Usage:
    j2.py [--site=SITEVARS] [--page=PAGEVARS] TEMPLATE [VARFILES...]

Options:
    -s --site SITEVARS      File containing variables to be stored under the "site" key
    -p --page PAGEVARS      File containing variables to be stored under the "page" key

Other VARFILES will be merged into the top level template context. They will
be processed in order, so duplicates are last value wins.
"""
from docopt import docopt

import json
import jinja2
import logging
import yaml

logging.basicConfig(level=logging.INFO)
arguments = docopt(__doc__)
logging.debug(arguments)


def loadfile(filename):
    if filename.endswith('.json'):
        with open(filename) as fp:
            data = json.load(fp)
    elif filename.endswith('.yml') or filename.endswith('.yaml'):
        with open(filename) as fp:
            data = yaml.load(fp)
    else:
        logging.error("Unrecognized file type. Data files must be JSON or YAML.")
        exit(1)
    return data


# load up the template context
context = {}

for varfile in arguments['VARFILES']:
    context.update(loadfile(varfile))

if arguments.get('--site', None):
    context['site'] = loadfile(arguments['--site'])

if arguments.get('--page', None):
    context['page'] = loadfile(arguments['--page'])

# FIXME to make relative URLs work, need to set siteroot. This only works
# because I happen to know that the site root is at build/html/. Need a
# clean way to do this.
numslashes = context['page']['path'].count("/") - 2
context['siteroot'] = "../" * numslashes

# Okay we have our context, now let's load the template
with open(arguments['TEMPLATE']) as fp:
    tpl = fp.read()

template = jinja2.Template(tpl)
output = template.render(context)
print(output)
