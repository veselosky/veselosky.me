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

THEME = 'themes/bootstrap3'
#THEME = 'notmyidea'
BOOTSTRAP_THEME = 'readable'
AVATAR = "http://www.gravatar.com/avatar/33eee43f62cad4b6001bbc9d48e30714.png"

MENUITEMS = (
        ('Category 1', '/cat1'),
        ('Category 2', '/cat2'),
        )
# Blogroll
LINKS =  (('Control-Escape: Linux Help', 'http://www.control-escape.com/'),
          ('Outline of History', 'http://outline-of-history.mindvessel.net/'),
          ('Webquills', 'http://www.webquills.net/'),
          )

# Social widget
SOCIAL = (('@veselosky', 'https://twitter.com/veselosky'),
        ('Resumé', 'https://linkedin.com/in/veselosky'),
        ('Code', 'https://github.com/veselosky/'),
        ('Facebook', 'https://facebook.com/veselosky/'),
        ('Google Plus', 'https://plus.google.com/+VinceVeselosky'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
