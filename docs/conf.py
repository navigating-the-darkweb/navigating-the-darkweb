# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime

project = 'Navigating the Dark Web'
copyright = f"2024-{datetime.now().year}, Sébastien Damaye"
author = 'Sébastien Damaye'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_fontawesome',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/favicon.ico'

# Check sidebar documentation
# https://sphinx-book-theme.readthedocs.io/en/stable/sections/sidebar-primary.html

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/navigating-the-darkweb/navigating-the-darkweb",
    "use_repository_button": False,
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    "use_download_button": False,
    #"show_toc_level": 4, # secondary navar auto-expands when reading. Can force static num of levels to be shown in secondary navbar
    #"show_navbar_depth": 1, # level of toc items in the left sidebar to remain expanded. Default=1
    #"max_navbar_depth": 4, # level of toc items included in the left sidebar. Default=4
    #"collapse_navbar": True, # allows (False) the left navbar to be expanded. Default=False
    "logo": {
        #"image_light": "_static/logo-light.png",
        #"image_dark": "_static/logo-dark.png",
        "text": "Navigating the Dark Web: A Comprehensive Guide to Darknets, Tools, and Intelligence",
        #"text": "Navigating the Dark Web",
    },
    "icon_links": [
        {
            "name": "Donate",
            "url": "https://www.paypal.com/donate/?hosted_button_id=WFXYUYZK2Y7DA",
            "icon": "fas fa-donate",
        },
    ],
}

"""
html_sidebars = {
    "**": ["navbar-logo.html", "icon-links.html", "search-button-field.html", "sbt-sidebar-nav.html"]
}
"""

pygments_style = 'sphinx'
