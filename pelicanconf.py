#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Basic Settings
AUTHOR = 'Kazi Fodor'
SITENAME = 'Stokori'
SITESUBTITLE = 'Multimedia Artist & Programmer'
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

DEFAULT_DATE_FORMAT = '%B %Y'

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/stokori'),
          ('Tumblr', 'http://stokori.tumblr.com'),
          ('GitHub', 'http://github.com/stokori'))

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# URL customization
ARTICLE_URL = "{category}/{slug}/"
ARTICLE_SAVE_AS = "{category}/{slug}/index.html"

CATEGORY_URL = "art/{slug}/"
CATEGORY_SAVE_AS = "art/{slug}/index.html"

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

ARCHIVES_SAVE_AS = 'archives/index.html'

INDEX_SAVE_AS = 'art/index.html'
INDEX_URL = "art/"

TEMPLATE_PAGES = {
    '../theme/templates/home.html': 'index.html',
}

# I highly doubt there will be any authors other than me any time soon
AUTHOR_SAVE_AS = ""

# Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc','better_figures_and_images','summary','clean_summary','thumbnailer','subcategory']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Theme Configuration
THEME = 'theme/'
PROFILE_PICTURE = "theme/images/profile.png"
DESCRIPTION = "I'm Kazi and I like birds."
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# Disqus
DISQUS_SITENAME = "stokorius"

#Thumbnailer
IMAGE_PATH = 'images'
THUMBNAIL_DIR = 'thumbs'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_SIZES = {
    'vertical': '200x?',
    'horizontal': '?x300',
    'square': '200x200'
}

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