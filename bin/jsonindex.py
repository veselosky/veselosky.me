#!/usr/bin/env python
"""
JSON Indexer.

This script will create an index over the JSON post files fed to it, using
the date and category fields. The resulting index will be formatted as JSON
and written to STDOUT.

Usage:
    jsonindex.py <filename>...


"""
import logging
import json

from docopt import docopt

logging.basicConfig(level=logging.DEBUG)
arguments = docopt(__doc__)
index = {"entries": [], "categories": {}}
categories = {}  # keep track of seen categories

for infile in arguments['<filename>']:
    # do not reprocess our output file!
    if infile == 'build/html/index.json':
        continue

    logging.debug("Processing %s" % infile)
    with open(infile) as fp:
        post = json.load(fp)
    # create an index entry for the post
    entry = {
        "date": post['date'],
        "category": post.get('category', "Uncategorized"),
        "title": post['title'],
        "description": post.get('description', ""),
        "path": infile
    }
    index['entries'].append(entry)
    categories[entry['category']] = 1

# now that we have all the index entries, sort them by date
index['entries'].sort(reverse=True, key=lambda x: x['date'])

# and then compile list by category
for entry in index['entries']:
    if not entry['category'] in index['categories']:
        index['categories'][entry['category']] = []
    index['categories'][entry['category']].append(entry)

# done, write output
print(json.dumps(index, indent=2, sort_keys=True))
