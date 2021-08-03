#!/usr/bin/env python
from setuptools import setup

import re
VERSIONFILE="sktda/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

with open('README.md') as f:
    long_description = f.read()

setup(name='scikit-tda',
      version=verstr,
      description='Topological Data Analysis for humans',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Nathaniel Saul, Chris Tralie',
      author_email='nathaniel.saul@wsu.edu, chris.tralie@gmail.com',
      url='https://github.com/scikit-tda/scikit-tda',
      license='MIT',
      packages=['sktda'],
      include_package_data=True,
      install_requires=[
        # Common requirements
        'numpy',
        'scipy',
        'scikit-learn',
        'matplotlib',

        # Ripser
        'Cython',
        'ripser',

        # Persim
        'persim',

        # Kepler Mapper
        'pillow', # for some kmapper examples
        'kmapper',

        # tadasets
        'tadasets',
      ],
      extras_require={
        'testing': [ # `pip install -e ".[testing]"``
            'pytest'
        ],
        'docs': [ # `pip install -e ".[docs]"``
            'sktda_docs_config',
            'pyyaml'
        ]
      },
      python_requires='>3.3',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
      ],
      keywords='topology data analysis, algebraic topology, unsupervised learning, persistent homology, persistence images, persistence diagrams, uniform manifold approximation and projection, sheaf theory, mapper, data visualization'
     )
