
|DOI| |Pypi| |Downloads|

Scikit-TDA is a home for Topological Data Analysis Python libraries intended for non-topologists. This project aims to provide a curated library of TDA Python tools that are widely usable and easily approachable.

The structure of these libraries is inspired by the `Tidyverse <https://tidyverse.org>`_ in that each package can stand alone and can be installed individually but each adheres to the same design principles. Further, the most benefit comes from using all of them together. You'll notice that in many of the examples and notebooks, multiple libraries are used together.

This project is entirely a work in progress and still in an early phase.
We hope to assemble an ecosystem of TDA libraries that is approachable to people outside the field of Algebraic Topology, complete with documentation, notebooks, and examples to get you up to speed.

If you would like to contribute, please reach out to us on github_, twitter_ or on slack_.


Install
---------

Installation of all libraries can be done directly from Pypi in one command.

::

  pip install scikit-tda


Contact
----------

If you would like to contribute and have ideas for how to do so, please reach out!
You can join us at `scikit-tda.slack.com` or follow us on twitter `@scikit_tda <https://twitter.com/scikit_tda>`_.
If you have any issues or confusion while using the library, please let us know with a github_ issue. We will try to respond quickly.


Contributing
---------------

Contributions are more than welcome! There are lots of opportunities for potential projects, so please get in touch if you would like to help out. Everything from code to notebooks to examples and documentation are all equally valuable so please don't feel you can't contribute. To contribute please fork the project make your changes and submit a pull request. We will do our best to work through any issues with you and get your code merged into the main branch.

Citation
-----------

For the time being, if you would like to cite Scikit-TDA, please use the following citation/bibtex:

    Saul, Nathaniel and Tralie, Chris. (2019). Scikit-TDA: Topological Data Analysis for Python. Zenodo. http://doi.org/10.5281/zenodo.2533369


::

    @misc{scikittda2019,
        author       = {Nathaniel Saul and Chris Tralie},
        title        = {Scikit-TDA: Topological Data Analysis for Python},
        year         = 2019,
        doi          = {10.5281/zenodo.2533369},
        url          = {https://doi.org/10.5281/zenodo.2533369}
    }

.. _github: https://github.com/scikit-tda


License
-----------

This package is licensed with the MIT license.


.. toctree::
    :maxdepth: 2
    :hidden:
    :caption: User Guide

    theory
    libraries
    

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Tutorials

    notebooks/scikit-tda Tutorial



.. |DOI| image:: https://zenodo.org/badge/129452930.svg
  :target: https://zenodo.org/badge/latestdoi/129452930
.. |Pypi| image:: https://badge.fury.io/py/scikit-tda.svg
  :target: https://badge.fury.io/py/scikit-tda
.. |Downloads| image:: https://pypip.in/download/scikit-tda/badge.svg
  :target: https://pypi.python.org/scikit-tda/sktda/

.. _github: https://github.com/scikit-tda
.. _twitter: https://twitter.com/scikit_tda
.. _slack: https://scikit-tda.slack.com

.. _Ripser: http://ripser.scikit-tda.org
.. _Persim: http://persim.scikit-tda.org
.. _Kepler-Mapper: http://kepler-mapper.scikit-tda.org
.. _TaDAsets: https://tadasets.scikit-tda.org
.. _Cechmate: https://cechmate.scikit-tda.org
