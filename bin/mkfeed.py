#!/usr/bin/env python
"""
Make Feed.

Given a JSON index of entries, generate an Atom feed
and write it to STDOUT.

Usage:
    mkfeed.py [options] <filename>

Options:
    -r --root ROOT          The path to the "document root" of the web site.
                            Used to calculate relative URLs.

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
from __future__ import absolute_import, print_function, unicode_literals

import logging
import yaml

from docopt import docopt
from feedgen.feed import FeedGenerator
from os import path

logging.basicConfig(level=logging.DEBUG)
arguments = docopt(__doc__)

docroot = arguments.get('--root', './')

index = yaml.load(open(arguments['<filename>']))

f = FeedGenerator()
f.title(index['title'])
f.author(name=index['author'])
f.link(href=index['link'], rel='alternate')
f.id(index['link'])

for entry in index['entries']:
    econtent = yaml.load(open(path.join(docroot, entry['path'] + '.json')))
    e = f.add_entry()
    e.id(':'.join(['tag', 'veselosky.com,' + entry['date'][:10], entry['path']]))
    e.title(entry['title'])
    e.link(href=index['link'] + entry['path'] + '.html', rel="alternate")
    e.summary(entry['description'])
    e.updated(entry['date'])
    e.published(entry['date'])
    e.content(econtent['_content'])

print(f.atom_str(pretty=True))

