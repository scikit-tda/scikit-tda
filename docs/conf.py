# -*- coding: utf-8 -*-
import os
import sys
import yaml

sys.path.insert(0, os.path.abspath("."))
sys.path.append(os.path.abspath("extensions"))
from sktda import __version__
from sktda_docs_config import *

project = "scikit-tda"
copyright = "2019, Nathaniel Saul"
author = "Nathaniel Saul"
version = __version__
release = __version__

html_theme_options.update(
    {
        # Google Analytics info
        "ga_ua": "UA-124965309-1",
        "ga_domain": "",
        "gh_url": "scikit-tda",
    }
)

html_short_title = project
htmlhelp_basename = "scikit-tdadoc"

html_context = {}

# Setup library data
with open("data/libraries.yaml", "r") as f:
    libraries = yaml.load(f, Loader=yaml.SafeLoader)


# import pdb; pdb.set_trace()
html_context["libraries"] = libraries

extensions.append("rstjinja")
