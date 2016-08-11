#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kazi Toko'
SITENAME = 'Stow it, Morte.'
SITEURL = 'http://stokori.us'

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/stokori'),
          ('Tumblr', 'http://stokori.tumblr.com'),
          ('GitHub', 'http://github.com/stokori'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins!
PLUGIN_PATHS = ['./pelican-plugins']
#PLUGINS = ['extract_toc','disqus_static','better_figures_and_images']
#MD_EXTENSIONS = (['toc'])

#Metadata
# EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    # 'extra/favicon.ico': {'path': 'favicon.ico'},
    # 'extra/htaccess': {'path': '.htaccess'}
# }