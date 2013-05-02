#!/usr/bin/env python
from distutils.core import setup
import os, sys

# Dynamically calculate the version based on colors.VERSION.
version = __import__('colors').get_version()
if u'SVN' in version:
    version = ' '.join(version.split(' ')[:-1])

setup(
    name = 'django-colors',
    version = version.replace(' ', '-'),
    description = 'Manipulate colors with django',
    packages = [
        'colors',
        'colors.templatetags'
    ],
    package_data={
        'colors': [
            'static/colors/js/*.js',
            'static/colors/css/*.css',
            'static/colors/images/*.png',
            'static/colors/images/*.gif',
            'templates/colors/*.html'
        ],
    },
    author = 'Maxime Haineault',
    author_email = 'max@motion-m.ca',
    url = 'http://code.google.com/p/django-colors/',
)

