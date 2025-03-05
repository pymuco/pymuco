# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os
import sys
from datetime import datetime

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('..'))

try:
    from recommonmark.parser import CommonMarkParser
except ImportError:
    CommonMarkParser = None

# ReadTheDocs specific configuration
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

# Only add ReadTheDocs extension if we're on ReadTheDocs
if on_rtd:
    extensions.append('readthedocs_ext.readthedocs')

templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
if CommonMarkParser:
    source_parsers = {
        '.md': CommonMarkParser,
    }
master_doc = 'index'
project = u'pymuco'
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_type_aliases = None

# Autodoc settings
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Output file base name for HTML help builder.
htmlhelp_basename = 'pymucodoc'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pymuco.tex', u'pymuco Documentation',
     u'German Margon', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/pymucologo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references in LaTeX output.
latex_show_pagerefs = False

# If true, show URL addresses after external links in LaTeX output.
latex_show_urls = False

# Documents to append as an appendix to all manuals.
latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pymuco', u'pymuco Documentation',
     [u'German Margon'], 1)
]

# If true, show URL addresses after external links in manual page output.
man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pymuco', u'pymuco Documentation',
     u'German Margon', 'pymuco', 'A Python Music Computation Library',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
texinfo_appendices = []

# If false, no module index is generated.
texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
texinfo_no_detailmenu = False

# If true, generate domain-specific indices in addition to the general index.
texinfo_domain_indices = True

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = u'German Margon'
epub_publisher = u'German Margon'
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
epub_basename = project

# The HTML theme for the epub output.
epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = ''

# A unique identification for the text.
epub_uid = ''

# A tuple containing the cover image and cover page html template
# filenames.
epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
epub_tocdepth = 3

# Allow duplicate toc entries.
epub_tocdup = True

# Choose between 'default' and 'includehidden'.
epub_tocscope = 'default'

# Fix section number references for epub
epub_fix_images = False
epub_unzip = False

# Blank short titles go into the parent.
epub_short_titles = True

# User's Sphinx configurations
language_user = globals().get('language', None)
latex_engine_user = globals().get('latex_engine', None)
latex_elements_user = globals().get('latex_elements', None)

# Remove this once xindy gets installed in Docker image and XINDYOPS
# env variable is supported
# https://github.com/rtfd/readthedocs-docker-images/pull/98
latex_use_xindy = False

chinese = any([
    language_user in ('zh_CN', 'zh_TW'),
    project_language in ('zh_CN', 'zh_TW'),
])

japanese = any([
    language_user == 'ja',
    project_language == 'ja',
])

if chinese:
    latex_engine = latex_engine_user or 'xelatex'

    latex_elements_rtd = {
        'preamble': '\\usepackage[UTF8]{ctex}\n',
    }
    latex_elements = latex_elements_user or latex_elements_rtd
elif japanese:
    latex_engine = latex_engine_user or 'platex'

# Make sure our build directory is always excluded
exclude_patterns = globals().get('exclude_patterns', [])
exclude_patterns.extend(['_build'])