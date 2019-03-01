.. _libraries:

Libraries 
===========

Scikit-TDA provides a complete suite of TDA tools designed for academic or industry uses. 

To install the entire suite

.. code:: python

  >>> pip install scikit-tda

Below, you'll find information on each individual package, along with resources to explore more. Each package is well tested, well documented, easy to install, and open for contributions. If you find any bugs in the code or documentation, please let us know on `github <https://github.com/scikit-tda>`_


{% for library in libraries %}
.. raw:: html

  <hr>


.. image:: logos/{{ library["logo"]}}
  :height: 130 px
  :alt: logo for cec
  :align: right
  :target: https://{{ library["url"] }}

{{ library["title"] }} 
----------------------------------------------------


.. image:: https://badge.fury.io/py/{{ library["pypi" ]}}.svg
  :target: https://badge.fury.io/py/{{ library["pypi" ]}}
.. image:: https://pypip.in/download/{{ library["pypi"] }}/badge.svg
  :target: https://pypi.python.org/pypi/{{ library["pypi"] }}/
.. image:: https://travis-ci.org/scikit-tda/{{ library["repo"] }}.svg?branch=master
  :target: https://travis-ci.org/scikit-tda/{{ library["repo"] }}
.. image:: https://codecov.io/gh/scikit-tda/{{ library["repo"] }}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/scikit-tda/{{ library["repo"] }}
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
  :target: https://opensource.org/licenses/MIT)


.. container:: 


{{ library["text"] }}


  Installation is as easy as 

  .. code:: python

    >>> pip install {{ library["pypi"] }}
        
  Check out complete documentation for {{ library["title"] }} at `{{ library["url"] }} <https://{{ library["url"] }}>`_ and the source code at `github.com/scikit-tda/{{ library["repo"] }} <https://github.com/scikit-tda/{{ library["repo"] }}>`_


{% endfor %}

