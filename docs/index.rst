.. scikit-tda documentation master file, created by
   sphinx-quickstart on Tue Jul 17 22:39:10 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Scikit-TDA!
======================================


There is a growing need for an ecosystem of TDA libraries that is approachable to non-researchers. This project aims to provide a curated library for Python tools that are widely usable and easily approachable. Each is easy to install through traditional Python mechanisms, portable to all platforms, requires no dependencies outside of what is available on Pypi, has comprehensive documentation , is open source, provides an issue tracker and is responsive to questions, and exposes an intuitive API for developers familiar with the Python scientific computing ecosystem.

Each project can stand alone, or be used as part of the scikit-tda bundle. This project curates the group of packages and houses extensive documentation and examples on how each package can be used together.

Scikit-TDA is a home for compatible TDA libraries intended for non-researchers. We provide detailed documentation and unified APIs so that using TDA can be used in the wild.

- Mapper ecosystem,
- Persistent Homology ecosystem,
- Dimensionality Reduction

The TDA ecosystem is rapidly growing. Below is the list of current projects, either built or in development, to be included in scikit-tda.

- **Ripser** - Data to diagrams in one line
- **Persim** - Easy Persistence Images
- **UMAP** - Mathematically justified dimensionality reduction
- **Kepler Mapper** - Mapper framework integrated into sklearn

Under Development
~~~~~~~~~~~~~~~~~~

- **Diagrams** - Comparison & Visualization of diagrams
- **TaDAsets** - Data sets designed for TDA
- **Cechmate** - Custom filtrations builder

Install
---------

Installation of all libraries can be done directly from Pypi in one command.

``pip install scikit-tda``

Issues & Contributions
------------------------

If you have any issues with the library, please let us know with a github issue, we will try to be responsive as possible.


.. toctree::
   :hidden:

   self

.. toctree::
    :maxdepth: 2

    about
    libraries/index

.. toctree::
    :maxdepth: 1
    :caption: tutorials

    tutorials/diagrams-on-umap
    tutorials/visualizing-cycles-with-umap
    tutorials/classification-of-persistence-images


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
