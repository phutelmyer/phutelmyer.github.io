#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://paulhutelmyer.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# A boolean for checking if feeds are turned on
FEEDS_ON = any([FEED_ALL_ATOM,
                CATEGORY_FEED_ATOM,
                TRANSLATION_FEED_ATOM,
                AUTHOR_FEED_ATOM,
                AUTHOR_FEED_RSS
])

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
