
Persim 
------

|PyPI version| |Build Status| |Codecov|


Persim is a Python implementation of Persistence Images as first introduced in `https://arxiv.org/abs/1507.06217 <https://arxiv.org/abs/1507.06217>`_.

It is designed to interface with `Ripser <https://github.com/sauln/ripser>`_, though any persistence diagram should work fine.

Setup
=======

Currently, the only option is to install the library from source:

.. code::

    pip install persim



Usage
======

First, construct a diagram. In this example, we will use [Ripser](https://github.com/sauln/ripser).

.. code::

    import numpy as np
    from ripser import Rips

    data = np.random.random((100,2))
    rips = Rips()
    dgm = rips.fit_transform(data)
    diagram = dgm[1] # Just diagram for H1


Then from this diagram, we construct the persistence image

.. code::

    from persim import PersImage

    pim = PersImage(diagram)
    img = pim.transform()
    pim.show(img)



References
============

Persistence Images were first introduced in `Adams et al, 2017 <http://www.jmlr.org/papers/volume18/16-337/16-337.pdf>`_. Much of this work, an examples contained herein are inspired by the work of `Obayashi and Hiraoka, 2017 <https://arxiv.org/abs/1706.10082>`_. Choices of weightings and general methods are often derived from `Kusano, Fukumizu, and Yasuaki Hiraoka, 2016 <https://arxiv.org/abs/1601.01741>`_.

Disclaimer
============

Standard MIT disclaimer applies, see ``DISCLAIMER.md`` for full text.

Development status is Alpha.




.. |PyPI version| image:: https://badge.fury.io/py/persim.svg
   :target: https://badge.fury.io/py/persim
.. |Build Status| image:: https://travis-ci.org/sauln/persim.svg?branch=master
   :target: https://travis-ci.org/sauln/persim
.. |Codecov| image:: https://codecov.io/gh/sauln/persim/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/sauln/persim



