.PHONY: clean-pyc clean-build docs clean json html posts
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "site - build the entire web site"
	@echo "json - build only the data files for the site, no html"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"


# Markdown files are converted to JSON output
build/html/%.json: content/%.md
	@mkdir -p $(@D)  # `dirname $@`
	@./bin/md2json.py $^ $@

# Inventory the source files, make list of dest files to target
JSONPOSTS = $(shell find content -name "*.md" | sed s/content/build\\/html/ | sed s/.md/.json/)

# After building individual posts, generate an index over them
build/html/index.json: $(JSONPOSTS)
	@./bin/jsonindex.py $(JSONPOSTS) > build/html/index.json

# Just an easy target to type, to build out all json files
json: build/html/index.json

# HTML pages are produced by feeding a context to a template. The context is
# constructed from the post JSON file, the index, and a site-wide variables
# file.
build/html/%.html: json
	./bin/j2.py -r build/html -s site.yml -p $(@:.html=.json) templates/page.html > $@
POSTS = $(JSONPOSTS:.json=.html)
posts: ${POSTS}

site: posts
	mkdir -p build/html/assets
	cp -r static/* build/html/assets/
# TODO combine and minify CSS, JS
# TODO List of index pages. How to manage these?


clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

test:
	python setup.py test

test-all:
	tox
