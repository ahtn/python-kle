#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

from setuptools import setup

setup(
    name = 'kle',
    version = '0.0.0',
    description = "Python library for parsing keyboard layout files from "
        "keyboard-layout-editor.com.",
    url = "http://github.com/ahtn/python-kle",
    author = "jem",
    author_email = "jem@seethis.link",
    license = 'MIT',
    packages = ['kle'],
    install_requires = [ 'six' ],
    keywords = ['keyboard', 'keyboard-layout-editor'],
    zip_safe = False
)
