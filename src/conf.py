# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'RBPBench'
copyright = '2023, BackofenLab, University of Freiburg'
author = 'Michael Uhl'

# The full version, including alpha/beta/rc tags
release = '2023'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",  # Markdown support
    "sphinxcontrib.bibtex",  # BibTex support
]

bibtex_bibfiles = ['references.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

def setup(app):
    app.add_css_file('my_theme.css')

# Create custom css for the webpage
html_static_path = ["assets/CSS", "assets/images"]
html_css_files = ["custom.css"]



html_sidebars = {
    '**': [
        # 'about.html',
        'navigation.html',
        'relations.html',  # Optionally include this if you want "next" and "previous" links
        # 'searchbox.html'  # This line is commented out or removed to exclude the search box
    ]
}


# html_sidebars = {
#     '**': [
#         #'custom_sidebar.html',  # Your custom template
#         'navigation.html',
#         #'searchbox.html',
#         # Add other sidebar elements as needed
#     ]
# }


html_logo = "assets/images/some_logo.png"

html_theme_options = {

    #'logo_only': False, 
    'nosidebar': False,
    #'show_relbar_bottom': True,
    'sidebar_width': '225px',
    #'sidebar_depth': 2,
}
html_title = "RBPBench Website"
