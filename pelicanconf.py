#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Joonas Haapala'
SITENAME = u'Haapa.la'
SITEURL = 'http://haapa.la'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_DATE = (2019, 8, 8, 14, 0, 0)
GOOGLE_ANALYTICS='UA-9759259-5'

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),
          )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = None

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

STATIC_PATHS = ['extra/favicon.ico', 'images']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = 10
#DEFAULT_CATEGORY = ''

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#THEME = "/home/joonas/src/pelican-themes/monospace"
THEME = "monospace"
#THEME = "subtle"

IMAGE_PATH='/content/images'
THUMBNAIL_DIR='/output/thumbnails'

PLUGIN_PATH = ['/home/joonas/src/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video', 'latex']#, 'thumbnailer', 'gallery']

MENUITEMS = [
    #('Home','/'),
    ('Github', 'https://github.com/Jontte?tab=repositories'),
]
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

#LOAD_CONTENT_CACHE = False

#PAGE_PATHS = ['pages']

DIRECT_TEMPLATES = ('index', 'archives')

