#!/usr/bin/env python
"""
Jinja2 template renderer.

This script will render a jinja2 template to STDOUT. The template context is
constructed from data files fed to the script.

Usage:
    j2.py [options] TEMPLATE [VARFILES...]

Options:
    -s --site SITEVARS      File containing variables to be stored under the
                            "site" key
    -p --page PAGEVARS      File containing variables to be stored under the
                            "page" key
    -r --root ROOT          The path to the "document root" of the web site.
                            Used to calculate relative URLs.

Other VARFILES will be merged into the top level template context. They will
be processed in order, so duplicates are last value wins.
"""
from docopt import docopt
from os import path

import jinja2
import logging
import yaml

logging.basicConfig(level=logging.INFO)
arguments = docopt(__doc__)
logging.debug(arguments)


def loadfile(filename):
    # json is a subset of yaml, so the yaml parser can handle both! yay!
    try:
        with open(filename) as fp:
            data = yaml.load(fp)
    except yaml.ScannerError:
        logging.error("Unrecognized file type. Data files must be JSON or YAML.") # noqa
        exit(1)
    return data


# load up the template context
context = {}

for varfile in arguments['VARFILES']:
    context.update(loadfile(varfile))

if arguments['--site']:
    context['site'] = loadfile(arguments['--site'])

if arguments['--page']:
    context['page'] = loadfile(arguments['--page'])

docroot = './'
if arguments['--root']:
    docroot = path.abspath(arguments['--root'])

logging.debug(context)
numslashes = path.relpath(context['page']['path'], docroot).count("/")
context['siteroot'] = "../" * numslashes

# Okay we have our context, now let's load the template
with open(arguments['TEMPLATE']) as fp:
    tpl = fp.read()

template = jinja2.Template(tpl)
output = template.render(context)
print(output)
