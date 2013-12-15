#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Tools and build instructions
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
TIMEZONE = 'America/New_York'

# General Site Appearance
AUTHOR = u'Vince Veselosky'
DEFAULT_CATEGORY = "Life"
DISPLAY_PAGES_ON_MENU = False
SITENAME = u'Vince Veselosky'
SITEURL = 'vince.veselosky.me'
SITESUBTITLE = u'Web Application Architect, Systems Specialist'
TYPOGRIFY = True
USE_FOLDER_AS_CATEGORY = False

# URL Configuration
ARCHIVE_SAVE_AS = 'archives.html'
# Pelican does not currently support direct source_path->dest_path
# translation. Fortunately, this pattern is backward compatible with
# the old Blogger URLs. -VV 2013-12-14
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.{lang}.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}.{lang}.html'
AUTHOR_SAVE_AS = None
AUTHORS_SAVE_AS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
FEED_ATOM = 'feeds/recent.atom'
FEED_DOMAIN = SITEURL
# FEED_MAX_ITEMS = 25
FEED_RSS = 'feeds/recent.rss'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_LANG_SAVE_AS = '{slug}.{lang}.html'
PAGE_LANG_URL = '{slug}.{lang}.html'
TAG_SAVE_AS = None
TAGS_SAVE_AS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

# Theme and Template Customizations
#THEME = 'notmyidea'
THEME = 'themes/bootstrap3'
BOOTSTRAP_THEME = 'readable'
AVATAR = "http://www.gravatar.com/avatar/33eee43f62cad4b6001bbc9d48e30714.png"
GITHUB_USER = "veselosky"
#GITHUB_SHOW_USER_LINK = True
GITHUB_REPO_COUNT = 3

MENUITEMS = ()
# Sidebar linkroll
LINKS =  (('Control-Escape: Linux Help', 'http://www.control-escape.com/'),
          ('Outline of History', 'http://outline-of-history.mindvessel.net/'),
          ('Webquills', 'http://www.webquills.net/'),
          )

# Sidebar Social Links
SOCIAL = (('@veselosky', 'https://twitter.com/veselosky'),
        ('Resumé', 'https://linkedin.com/in/veselosky'),
        ('Code', 'https://github.com/veselosky/'),
        ('Facebook', 'https://facebook.com/veselosky/'),
        ('Google Plus', 'https://plus.google.com/+VinceVeselosky'),
        )

