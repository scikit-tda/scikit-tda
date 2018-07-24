UMAP
======================================

UMAP provides a dimensionality reduction algorithm that is built on theory as beautiful as the results it produces. 

For complete documentation, see UMAP_. 

Quick start
--------------

.. code:: python

    import umap
    import numpy as np

    data = np.random.random((1000,10))
    reduced = UMAP().fit_transform(data)

.. _UMAP: https://umap.scikit-tda.org
