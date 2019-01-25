.. _libraries:

Libraries 
===========

Scikit-TDA provides a complete suite of TDA tools designed for academic or industry uses. 
Ripser provides an easy interface for constructing persistence diagrams and Persim houses many tools for comparing diagrams. 
Kepler-Mapper is a package for constructing and viewing Mapper from a data set, leveraging scikit-learn for as much processing as possible. 


Scikit-TDA libraries are structured similarly to the `Tidyverse <https://tidyverse.org>`_ in that each package can stand alone, can be installed individually, but adheres to the design principles of the library. 



{% for library in libraries %}
{{ library["title"] }}
-------------------------

{{ library["text"] }}

Check out complete documentation for {{ library["title"] }} at `{{ library["url"] }} <https://{{ library["url"] }}>`_.
{% endfor %}
