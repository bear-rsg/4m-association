#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Base configuration
AUTHOR = '4M Association'
SITENAME = '4M Association'
PATH = 'content'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Appearance
THEME = './active-theme/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGINS = ['assets', 'sitemap', 'pelican-page-hierarchy','i18n_subsites']


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
PLUGIN_PATHS = ['./pelican-plugins/']
I18N_TEMPLATES_LANG = 'en'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False

PATH_METADATA = 'articles/(?P<path>.*)\..*'

DEFAULT_METADATA = { }

ARTICLE_SAVE_AS = '{path}/{slug}.html'
ARTICLE_URL = '{path}/{slug}.html'
ARTICLE_ORDER_BY = 'reversed-date'

ARTICLE_EXCLUDES = ['templates']
TEMPLATE_PAGES = {
}

# Don't need the author pages
AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'basename'
INDEX_SAVE_AS = 'index.html'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git', '.gitignore']
#
# SITEMAP PLUGIN
#
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DEFAULT_DATE_FORMAT = ('%d-%m-%Y')

SITEURL = '.'

# Static files
STATIC_PATHS = [
    'images',
    'css',
    'assets',
]

# EXTRA_PATH_METADATA = {
#     'extra/custom.css': {'path': 'custom.css'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'},
#     'extra/CNAME': {'path': 'CNAME'},
#     'extra/README': {'path': 'README'},
# }
# IGNORE_FILES = ['.#*', 'README.md']

DEFAULT_PAGINATION = 10

# URL settings
SLUGIFY_SOURCE = 'basename'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
# ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
# Don't need the author pages
# AUTHOR_SAVE_AS = ''
# AUTHOR_URL = ''
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Home', '/welcome.html'),
    ('About', '/about.html'),
    ('Interest Groups', '/interest-groups.html'),
    ('Projects', '/projects.html'),
    ('Join 4M', '/join4m.html'),
    ('Bulletin', '/bulletin/bulletin-index.html'),
    ('4M Conference Series', '/conference/conference-index.html'),
    ('Expert Workshop FOCUS', '/bulletin/2016/September/Expert-Workshop-FOCUS/expert-workshop-focus.html'),
)

LOCALE = ('en_GB', 'en')
