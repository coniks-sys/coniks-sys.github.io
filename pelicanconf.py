#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CONIKS Team'
SITENAME = 'CONIKS'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%m-%d-%Y'

ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
PAGE_ORDER_BY = 'page-order'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_OPEN_GRAPH = False

# Social widget
SOCIAL = (('github', 'https://github.com/coniks-sys'),
('twitter', 'http://twitter.com/coniks_sys'))

DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_NEWS = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False;

THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

STATIC_PATHS = ['static/Rochlin_Michael.pdf']
ARTICLE_PATHS = ['news']

#SITELOGO = 'static/logo.png'
#HIDE_SITENAME = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
