#!/usr/bin/env python
"""
JSON Indexer.

This script will create an index over the JSON post files fed to it, using
the date and category fields. The resulting index will be formatted as JSON
and written to STDOUT.

Usage:
    jsonindex.py -s YAML [-r ROOT] <filename>...

Options:
    -r --root ROOT          The path to the "document root" of the web site.
                            Used to calculate relative URLs.
    -s --site YAML          Your site.yml file, needed for metadata.

Index Format:

TODO JSON Schema
TODO Explain path manipulation

    entry = {
        "date": post['date'],
        "category": post.get('category', "Uncategorized"),
        "title": post['title'],
        "description": post.get('description', ""),
        "path": path.splitext(path.relpath(infile, docroot))[0],
    }


"""
import logging
import json
import yaml

from docopt import docopt
from os import path

logging.basicConfig(level=logging.DEBUG)
arguments = docopt(__doc__)
index = {"entries": [], "categories": {}}
docroot = './'
if arguments['--root']:
    docroot = path.abspath(arguments['--root'])

conf = yaml.load(open(arguments['--site']))
index['title'] = conf['site']['title']
index['author'] = conf['site']['author']
index['link'] = conf['site']['base']

for infile in arguments['<filename>']:

    logging.debug("Processing %s" % infile)
    with open(infile) as fp:
        post = json.load(fp)
    # create an index entry for the post
    try:
        entry = {
            "date": post['date'],
            "category": post.get('category', "Uncategorized"),
            "title": post['title'],
            "description": post.get('description', ""),
            # intentionally remove extension, see docs
            "path": path.splitext(path.relpath(infile, docroot))[0],
        }
    except KeyError:
        # If required fields are missing, this is not an indexable page.
        logging.warn("Missing date or title, unable to index: %s" % infile)
        continue

    index['entries'].append(entry)

# now that we have all the index entries, sort them by date
index['entries'].sort(reverse=True, key=lambda x: x['date'])

# and then compile list by category
for entry in index['entries']:
    if entry['category'] not in index['categories']:
        index['categories'][entry['category']] = []
    index['categories'][entry['category']].append(entry)

# done, write output
print(json.dumps(index, indent=2, sort_keys=True))
