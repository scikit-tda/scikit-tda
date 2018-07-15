This is essentially two projects, one is the conglomerate documentation and the other is the conglomerate packages.

Installing all packages is straight forward, it's hard to incorporate all of the documentation.  What is the best way to do this?

Should we have all the docs included as well? No point in hosting them all twice?



# Scikit-TDA

Scikit-TDA is an opinionated collection of libraries for Topological Data Analysis. The user interfaces across all included libraries are standardized and compatible with numpy and scikit-learn.

This is currently a WIP. Documentation and examples will be coming this summer.

Currently, we include
- [Kepler Mapper](https://github.com/MLWave/kepler-mapper) for mapper and visualization.
- [UMAP](https://github.com/lmcinnes/UMAP) for dimensionality reduction.
- [ripser](https://github.com/ctralie/ripser) for persistent homology.
- [persim](https://github.com/sauln/persim) for persistence images.


To install all these libraries
```
    pip install scikit-tda
```


The libraries will then be accessible from `sktda`

``` Python
    import sktda.kmapper as km
```

*It is not clear what the best way to do this is.  Should all libraries exist at the top level, or should we reorganize the libraries so they make more sense as a group?* 

# Adding new libraries

All the magic happens in [Makefile](Makefile).

It works by including each library as a submodule, 

