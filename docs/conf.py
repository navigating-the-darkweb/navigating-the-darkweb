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
    #'sphinx.ext.autosectionlabel',
    #'sphinx_design',
    #'sphinx_togglebutton',
    'sphinx_fontawesome',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

numfig = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']
html_css_files = ['custom.css']
html_favicon = '_static/favicon.ico'

html_title = 'Navigating the Dark Web'

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
    "use_sidenotes": True, # puts footnotes in the margin instead of at the bottom of the page
    #"show_navbar_depth": 4, # level of toc items in the left sidebar to remain expanded. Default=1
    #"max_navbar_depth": 4, # level of toc items included in the left sidebar. Default=4
    #"navigation_depth": 4,
    #"show_nav_level": 4,
    #"show_toc_level": 4, # secondary navar auto-expands when reading. Can force static num of levels to be shown in secondary navbar
    #"collapse_navbar": False, # allows (False) the left navbar to be expanded. Default=False
    "logo": {
        #"image_light": "_static/logo-light.png",
        #"image_dark": "_static/logo-dark.png",
        "text": "Navigating the Dark Web: A Comprehensive Guide to Darknets, Tools, and Intelligence",
        #"text": "Navigating the Dark Web",
    },
    "icon_links": [
        {
            "name": "Github project",
            "url": "https://github.com/navigating-the-darkweb/navigating-the-darkweb/",
            "icon": "fa-brands fa-github",
            "type": "fontawesome"
        },
        {
            "name": "Reddit",
            "url": "https://www.reddit.com/r/NavigatingTheDarkWeb/",
            "icon": "fa-brands fa-reddit",
            "type": "fontawesome"
        },
        {
            "name": "Email",
            "url": "https://spamty.eu/show/v6/11513/QovA91huoP7d2fe196v4migr/",
            "icon": "fas fa-envelope",
            "type": "fontawesome"
        },
        {
            "name": "Donate",
            "url": "https://www.paypal.com/donate?hosted_button_id=73UNLMZ6CC8C6",
            "icon": "fas fa-donate",
        },
    ],
    "home_page_in_toc": True # include welcome page to navigation bar on the left
 }

pygments_style = 'sphinx'
