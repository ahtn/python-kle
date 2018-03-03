#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

from setuptools import setup
import os

try: # python3
    fields = {}
    with open(os.path.join("kle", "version.py")) as f:
        exec(f.read(), fields)
    __version__ = fields['__version__']
except: # python2
    execfile(os.path.join("kle", "version.py"))

setup(
    name = 'kle',
    version = __version__,
    description = "Python library for parsing keyboard layout files from "
        "keyboard-layout-editor.com.",
    url = "http://github.com/ahtn/python-kle",
    author = "jem",
    author_email = "jem@seethis.link",
    license = 'MIT',
    packages = ['kle'],
    install_requires = [ 'six' ],
    keywords = ['keyboard', 'keyboard-layout-editor'],
    scripts = ['bin/kle-view'],
    zip_safe = False
)
