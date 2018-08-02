#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "QQLoginTool",
    version = "0.1.0",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "time and path tool",
    long_description = "time and path tool",
    license = "MIT Licence",

    url = "https://github.com/AugustHub/QQLogin.git",
    author = "august",
    author_email = "august@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [request]
)
