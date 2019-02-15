.. _libraries:

Libraries 
===========

Scikit-TDA provides a complete suite of TDA tools designed for academic or industry uses. 

The libraries are structured similarly to the `Tidyverse <https://tidyverse.org>`_ in that each package can stand alone, can be installed individually, but adheres to the design principles of the library. The most benefit comes from using all of them together. You'll notice in many of the examples and notebooks that often multiple libraries are used together.


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




.. container:: 


{{ library["text"] }}


  Installation is as easy as 

  .. code:: python

    >>> {{ library["install"] }}
        
  Check out complete documentation for {{ library["title"] }} at `{{ library["url"] }} <https://{{ library["url"] }}>`_.


{% endfor %}


{% for library in libraries %}



{% endfor %}