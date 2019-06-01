#######################################################################
# Makefile for building this web site.
#
# I'm not a Make magician so there's lots of room for improvement. The
# strategy is to convert input files to a standard JSON format, then
# use the JSON to create an index and provide variables to the templates.
#
# Currently only support Markdown sources, but any source format can be
# used if you can build a source to json converter. If you do, you'll
# need to adjust the JSONPOSTS declaration.
#######################################################################

SHELL := /bin/bash
SITEDIR = public
PROD = vince-veselosky-me

#######################################################################
# Build targets and rules
#######################################################################
.PHONY: clean-pyc clean-build docs clean json html posts

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "site - build entire web site, including HTML, styles, and scripts"
	@echo "serve - run a web server in the build directory"
	@echo "deploy - upload the files to the public server"


html:
	echo "TODO Build something"

dev:
	echo "TODO Build something"

site:
	gatsby build

serve:
	gatsby develop

clean:
	gatsby clean

deploy:
	aws s3 sync --acl public-read $(SITEDIR) s3://$(PROD)
	aws s3api put-bucket-website --bucket $(PROD) --website-configuration file://siteconfig.json
