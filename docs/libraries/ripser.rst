Ripser
======================================

The Ripser Python library is a wrapper around the amazing Ripser C++ library. It is super easy to install, provides an easy face, and is blazingly fast.

For complete documentation, see Ripser_.


Quick start
--------------

.. code:: python

    import numpy as np
    from ripser import ripser, plot_dgms

    data = np.random.random((100,2))
    diagrams = ripser(data)['dgms']
    plot_dgms(diagrams, show=True)





.. _Ripser: http://ripser.scikit-tda.org
