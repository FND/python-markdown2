#!/usr/bin/env python

import os
import sys
import distutils
from distutils.core import setup

_top_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_top_dir, "lib"))
try:
    import markdown2
finally:
    del sys.path[0]
README = open(os.path.join(_top_dir, 'README.txt')).read()

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Documentation
Topic :: Text Processing :: Filters
Topic :: Text Processing :: Markup :: HTML 
"""

if sys.version_info < (2, 3):
    # Distutils before Python 2.3 doesn't accept classifiers.
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

script = (sys.platform == "win32" and "lib\\markdown2.py" or "bin/markdown2")

setup(
    name="markdown2",
    version=markdown2.__version__,
    maintainer="Trent Mick",
    maintainer_email="trentm@gmail.com",
    author="Trent Mick",
    author_email="trentm@gmail.com",
    url="http://code.google.com/p/python-markdown2/",
    license="MIT",
    platforms=["any"],
    py_modules=["markdown2"],
    package_dir={"": "lib"},
    scripts=[script],
    description="A fast and complete Python implementaion of Markdown",
    classifiers=filter(None, classifiers.split("\n")),
    long_description=README,
)

