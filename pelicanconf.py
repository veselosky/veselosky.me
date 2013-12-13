#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vince Veselosky'
SITENAME = u'Vince Veselosky'
SITEURL = ''
SITESUBTITLE = u'Web Application Architect, Systems Specialist'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
TYPOGRIFY = True

FEED_ATOM = 'feeds/recent.atom'
FEED_RSS = 'feeds/recent.rss'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter: @veselosky', 'https://twitter.com/veselosky'),
        ('LinkedIn: veselosky', 'https://linkedin.com/in/veselosky'),
        ('Github: veselosky', 'https://github.com/veselosky/'),
        ('Facebook: veselosky', 'https://facebook.com/veselosky/'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
