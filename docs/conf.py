# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
# Modifica la ruta para apuntar al directorio raíz del proyecto (un nivel arriba del directorio docs)
sys.path.insert(0, os.path.abspath('..'))
project = 'LaplaceSolver'
copyright = '2025, Sebastian Acuña, Jose Luis Zamora.'
author = 'Sebastian Acuña, Jose Luis Zamora.'
release = '14/11/2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Si usas NumPy/Google style docstrings
]

