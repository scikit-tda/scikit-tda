#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='scikit-tda',
      version='0.0.1',
      description='Topological Data Analysis for humans',
      long_description=long_description,
      long_description_content_type="text/markdown",	
      author='Nathaniel Saul',
      author_email='nathaniel.saul@wsu.edu',
      url='https://github.com/sauln/scikit-tda',
      license='MIT',
      packages=['sktda'],
      include_package_data=True,
      install_requires=[
        # 'Cython', # Ripser isn't quite ready
        # 'ripser',
        'persim',
        'kmapper',
        'umap-learn'
      ],
      python_requires='!=3.1,!=3.2,!=3.3',
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
      ],
      keywords='topology data analysis, algebraic topology, unsupervised learning, persistent homology, persistence images, persistence diagrams, uniform manifold approximation and projection, sheaf theory, mapper, data visualization'
     )
