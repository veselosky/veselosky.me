# -*- coding: utf-8 -*-
# This file is execfile()d with the current directory set to its
# containing dir.
# Disable syntax checking because the number of complaints is INSANE
# flake8: noqa
import sys
import os

#import sphinx_bootstrap_theme
import alabaster

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'
extensions = [
    'alabaster',
    'chephren.website',
    'sphinx.ext.todo',
    'sphinxcontrib.embedly',
]
embedly_msg = "You MUST set the EMBEDLYKEY environment variable."
embedly_key = os.environ.get('EMBEDLYKEY', None)
if not embedly_key:
  raise embedly_msg

project = u'Vince Veselosky'
# HTML is included in the page. This is probably a bug, but useful for me.
copyright = u'''
2015 Vince Veselosky. | <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img
  alt="Creative Commons License" style="border-width:0"
  src="http://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>
  <br>
This work is licensed under
  <a rel="license"
  href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons
  Attribution-NonCommercial-NoDerivatives 4.0 International License</a>
'''
templates_path = ['../templates' ]  # relative to this directory.
source_suffix = '.rst'
source_encoding = 'utf-8'
master_doc = 'index'
base_url = 'http://vince.veselosky.me'
primary_domain = 'blog'
feed_filename = 'feeds/recent.atom'

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Vince Veselosky'
html_short_title = 'Vince Veselosky'
html_logo = '../extra/apple-touch-icon-precomposed.png'
#html_favicon = None
html_domain_indices = True
html_use_index = True
#html_split_index = False
#html_show_sourcelink = True
html_show_sphinx = False
#html_show_copyright = True
# Output file base name for HTML help builder.
htmlhelp_basename = 'OccamsMovingPartsdoc'

# Alabaster theme
html_theme = 'alabaster'
html_style = 'veselosky.css' # override theme style for customizations
html_theme_options = {
  'github_user': 'veselosky',
  'github_repo': 'veselosky.me',
  'logo_name': True,
  'logo_text_align': 'center',
  'description': 'Systems Architect, Web Applications',
  'analytics_id': 'UA-642116-10',
  'show_powered_by': False,
  'github_button': False,
}
html_sidebars = {
    '**': ['localtoc.html', 'relations.html']
}

# Bootstrap theme options
# html_theme_options = {
#     'bootswatch_theme': "readable",
#     'navbar_pagenav': False,
#     'navbar_sidebarrel': False,
#     'source_link_position': "footer",
# }
# html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['../extra']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'OccamsMovingParts.tex', u'Occam\'s Moving Parts Documentation',
   u'Vince Veselosky', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
