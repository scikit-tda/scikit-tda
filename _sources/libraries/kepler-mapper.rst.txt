Kepler Mapper
======================================

Kepler Mapper implements the Mapper algorithm (Singh, 2007). It provides a flexible API that leverages scikit-learn as much as possible. Additionally, the visualization interface built on D3 provides an interactive environment for exploring data.

For complete documentation, see KeplerMapper_.

Quick start
--------------------


.. code:: python

    import numpy as np
    import kmapper as km

    # Some sample data
    data = np.random.random((1000, 10))

    # Initialize
    mapper = km.KeplerMapper(verbose=1)

    # Construct lens on X-axis
    lens = mapper.fit_transform(data, projection=[0])

    # Construct the mapper graph with a lens cover of 10 cubes
    graph = mapper.map(lens, data, nr_cubes=10)

    # Visualize it and save to html files
    mapper.visualize(graph, path_html="keplermapper_output.html")

.. _KeplerMapper: https://kepler-mapper.scikit-tda.org