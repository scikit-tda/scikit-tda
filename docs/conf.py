# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('extensions'))
from sktda import __version__
from theme_settings import *

project = 'scikit-tda'
copyright = '2019, Nathaniel Saul'
author = 'Nathaniel Saul'
version = __version__
release = __version__

html_theme_options.update({
  # Google Analytics info
  'ga_ua': 'UA-124965309-1',
  'ga_domain': '',
})

html_short_title = project
htmlhelp_basename = 'scikit-tdadoc'

html_context = {}

# Setup library data
import yaml
with open('data/libraries.yaml', 'r') as f:
    libraries = yaml.load(f)


# import pdb; pdb.set_trace()
html_context['libraries'] = libraries

extensions.append('rstjinja')
