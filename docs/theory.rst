
.. _background:


Theory
============


Topology
----------------------------


Topology started with Leonhard Euler and the famous problem of the Seven Bridges of Königsberg: Can one construct a path that crosses each bridge exactly once and reaches all islands?

The fundamental assumption in topology is that connectivity is more important than distance. This lack of distinction is important to why topology is useful for analyzing data. Instead of getting wrapped up in myopic details of how far apart two points are, topology is concerned with qualitative questions, like: how many holes does the object have?, or: how many pieces is it constructed out of? Essentially, topology is a way to explore the shape of data without concern for things like which metric to use.

Fundamental shapes of data that can be studied with topology:

- linearities
- non-linearities
- clusters
- flares
- loops

Real-world data is often complex and contains multiple different fundamental shapes.


Topological Data Analysis
----------------------------

In applied mathematics, topological data analysis (TDA) is an approach to the analysis of datasets using techniques from topology. Extraction of information from datasets that are high-dimensional, incomplete and noisy is generally challenging. TDA provides a general framework to analyze such data in a manner that is insensitive to the particular metric chosen and provides dimensionality reduction and robustness to noise. Beyond this, it inherits functoriality, a fundamental concept of modern mathematics, from its topological nature, which allows it to adapt to new mathematical tools.

TDA offers:

- **A lossy compressed mathematical representation of a data set.** You can study the global structure of a dataset, down to the details of a single data point, without incurring a cognitive overload.
- **Resistance to noise and missing data.** TDA retains significant features of the data.
- **Invariance.** Only connectedness matters. The skew, size, or orientation of data does not fundamentally change that data.
- **A data exploration tool.** Get answers to questions you haven't even asked yet.
- **A methodology to study the shape of data and manifolds.** TDA has a solid theoretical foundation and inherits functoriality.



**Persistent homology** will identify loops or holes in high dimensions that might indicate some unrealized time dependent behavior.
This information can inform downstream analysis in many different ways.
Alternatively, topological structures in data sets might not be directly interpretable, but still provide excellent signatures for discriminating between multiple different sets.
In this context, the resulting persistence diagrams can be used as a feature in other machine learning models.

Another method from TDA is **Mapper**, which is designed to help you visualize and explore high dimensional data sets. Mapper will capture much of the critical topological structures as a graph which can be viewed in lower dimensions.


