#!/usr/bin/env python

from setuptools import setup, find_packages
import os

from bitcoinlib import __version__

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README')) as f:
    README = f.read()

requires = []

setup(name='python-bitcoinlib',
      version=__version__,
      description='The Swiss Army Knife of the Bitcoin protocol.',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
      ],
      url='https://github.com/petertodd/python-bitcoinlib',
      keywords='bitcoinlib',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      test_suite="bitcoinlib.tests"
     )
