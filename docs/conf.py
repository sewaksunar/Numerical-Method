# Configuration file for Sphinx documentation builder

project = 'Numerical Methods'
copyright = '2026'
author = 'Course Materials'
release = '1.0'

extensions = [
    'sphinx.ext.mathjax',
    'myst_parser',
    'sphinx_rtd_theme',
]

# Source file suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Theme
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
}

# Math rendering with MathJax
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'

# MyST parser settings for better markdown support
myst_enable_extensions = [
    "dollarmath",
    "colon_fence",
    "substitution",
]

# HTML output
import os
html_static_path = ['_static'] if os.path.exists('_static') else []
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.nojekyll']

# Master document
master_doc = 'index'
suppress_warnings = ['myst.header_anchor']
