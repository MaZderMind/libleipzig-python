# Copyright (C) 2009, 2010 Robert Lehmann
# Ported to python3 by Peter Körner 2014

from setuptools import setup
import os.path

setup(name='libleipzig',
      version='1.3-py3',
      description="wortschatz.uni-leipzig.de binding",
      long_description=open(os.path.join(os.path.dirname(__file__),
          "README.rst")).read(),
      url="http://github.com/MaZderMind/libleipzig-python/",
      install_requires = ['suds-jurko'],
      tests_require = ['nose'],
      test_suite = "nose.collector",
      author="Robert Lehmann, Peter Körner",
      author_email="libleipzig@robertlehmann.de, peter@mazdermind.de",
      license="GPLv3",
      packages=['libleipzig', 'libleipzig.test'],
      package_dir={'libleipzig.test': "tests"},
      package_data={'libleipzig': ["README.rst"]},
      entry_points={'console_scripts': ['wortschatz = libleipzig.main:main']},
      zip_safe=True,
      classifiers=[
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: German',
          'Topic :: Text Processing :: Linguistic',
        ],
)
