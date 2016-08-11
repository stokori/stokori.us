#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazi Toko'
SITENAME = 'I\'ll Think of Something Witty Eventually'
SITEURL = 'http://www.stokori.us'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/stokori'),
          ('Tumblr', 'http://stokori.tumblr.com'),
          ('GitHub', 'http://github.com/stokori'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# URL rewrites
ARTICLE_URL = "posts/{category}/{slug}/"
ARTICLE_SAVE_AS = "posts/{category}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

AUTHOR_URL = "author/{slug}/"
AUTHOR_SAVE_AS = "author/{slug}/index.html"

# Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','better_figures_and_images','summary','clean_summary','render_math']
MD_EXTENSIONS = (['toc'])

# Theme
THEME = 'theme/'

#Static Paths and Metadata
STATIC_PATHS = [
    'images', 
    'extra/robots.txt', 
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}