# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from datetime import datetime

from recommonmark.parser import CommonMarkParser

extensions = ["sphinx.ext.autodoc", "myst_parser"]
templates_path = ['templates', '_templates', '.templates']
source_suffix = ['.rst', '.md']
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
htmlhelp_basename = 'pymuco'
html_theme = 'sphinx_rtd_theme'
file_insertion_enabled = False
latex_documents = [
  ('index', 'pymuco.tex', u'pymuco Documentation',
   u'', 'manual'),
]




###########################################################################
#          auto-created readthedocs.org specific configuration            #
###########################################################################


#
# The following code was added during an automated build on readthedocs.org
# It is auto created and injected for every build. The result is based on the
# conf.py.tmpl file found in the readthedocs.org codebase:
# https://github.com/rtfd/readthedocs.org/blob/main/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl
#
# Note: this file shouldn't rely on extra dependencies.

import importlib
import sys
import os.path

# Borrowed from six.
PY3 = sys.version_info[0] == 3
string_types = str
sys.path.append(os.path.abspath('../pymuco'))
sys.path.append(os.path.abspath('../pymuco/test'))

from sphinx import version_info

# Get suffix for proper linking to GitHub
# This is deprecated in Sphinx 1.3+,
# as each page can have its own suffix
if globals().get('source_suffix', False):
    if isinstance(source_suffix, string_types):
        SUFFIX = source_suffix
    elif isinstance(source_suffix, (list, tuple)):
        # Sphinx >= 1.3 supports list/tuple to define multiple suffixes
        SUFFIX = source_suffix[0]
    elif isinstance(source_suffix, dict):
        # Sphinx >= 1.8 supports a mapping dictionary for multiple suffixes
        SUFFIX = list(source_suffix.keys())[0]  # make a ``list()`` for py2/py3 compatibility
    else:
        # default to .rst
        SUFFIX = '.rst'
else:
    SUFFIX = '.rst'

# Add RTD Static Path. Add to the end because it overwrites previous files.
if not 'html_static_path' in globals():
    html_static_path = []
if os.path.exists('_static'):
    html_static_path.append('_static')

# Add RTD Theme only if they aren't overriding it already
using_rtd_theme = (
    (
        'html_theme' in globals() and
        html_theme in ['default'] and
        # Allow people to bail with a hack of having an html_style
        'html_style' not in globals()
    ) or 'html_theme' not in globals()
)
if using_rtd_theme:
    html_theme = 'sphinx_rtd_theme'
    html_style = None
    html_theme_options = {}


# This following legacy behavior will gradually be sliced out until its deprecated and removed.
# Skipped for Sphinx 6+
# Skipped by internal Feature flag SKIP_SPHINX_HTML_THEME_PATH
# Skipped by all new projects since SKIP_SPHINX_HTML_THEME_PATH's introduction (jan 2023)
if (
        using_rtd_theme
        and version_info < (6,0)
        and not False
    ):
    theme = importlib.import_module('sphinx_rtd_theme')
    html_theme_path = [theme.get_html_theme_path()]

# Define websupport2_base_url and websupport2_static_url
if globals().get('websupport2_base_url', False):
    websupport2_base_url = 'https://readthedocs.org/websupport'
    websupport2_static_url = 'https://assets.readthedocs.org/static/'


#Add project information to the template context.
context = {
    'using_theme': using_rtd_theme,
    'html_theme': html_theme,
    'current_version': "latest",
    'version_slug': "latest",
    'MEDIA_URL': "https://media.readthedocs.org/",
    'STATIC_URL': "https://assets.readthedocs.org/static/",
    'PRODUCTION_DOMAIN': "readthedocs.org",
    'proxied_static_path': "/_/static/",
    'versions': [
    ("latest", "/en/latest/"),
    ],
    'downloads': [ 
    ],
    'subprojects': [ 
    ],
    'slug': 'pymuco',
    'name': u'pymuco',
    'rtd_language': u'en',
    'programming_language': u'words',
    'canonical_url': 'https://pymuco.readthedocs.io/en/latest/',
    'analytics_code': 'None',
    'single_version': False,
    'conf_py_path': '/docs/',
    'api_host': 'https://readthedocs.org',
    'github_user': 'LiamMZ',
    'proxied_api_host': '/_',
    'github_repo': 'pymuco',
    'github_version': 'main',
    'display_github': True,
    'bitbucket_user': 'None',
    'bitbucket_repo': 'None',
    'bitbucket_version': 'main',
    'display_bitbucket': False,
    'gitlab_user': 'None',
    'gitlab_repo': 'None',
    'gitlab_version': 'main',
    'display_gitlab': False,
    'READTHEDOCS': True,
    'using_theme': (html_theme == "default"),
    'new_theme': (html_theme == "sphinx_rtd_theme"),
    'source_suffix': SUFFIX,
    'ad_free': False,
    'docsearch_disabled': False,
    'user_analytics_code': '',
    'global_analytics_code': 'UA-17997319-1',
    'commit': '3b50f99d',
}

# For sphinx >=1.8 we can use html_baseurl to set the canonical URL.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_baseurl
if version_info >= (1, 8):
    if not globals().get('html_baseurl'):
        html_baseurl = context['canonical_url']
    context['canonical_url'] = None





html_context = context

# Add custom RTD extension
if 'extensions' in globals():
    # Insert at the beginning because it can interfere
    # with other extensions.
    # See https://github.com/rtfd/readthedocs.org/pull/4054
    extensions.insert(0, "readthedocs_ext.readthedocs")
else:
    extensions = ["readthedocs_ext.readthedocs"]

# Add External version warning banner to the external version documentation
if 'branch' == 'external':
    extensions.insert(1, "readthedocs_ext.external_version_warning")
    readthedocs_vcs_url = 'None'
    readthedocs_build_url = 'https://readthedocs.org/projects/pymuco/builds/20433790/'

project_language = 'en'

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