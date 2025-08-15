# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'House8848'
copyright = '2025, Marshal'
author = 'Marshal'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
	'myst_parser', 
	'sphinxcontrib.mermaid', 
    'sphinx-jsonschema'
]

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'

html_theme = 'sphinx_rtd_theme'
html_logo = "../static/ic_launcher_sphinx.png"
#html_logo = "_static/ic_launcher_blues.png"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../static']
html_show_sphinx = False
html_show_sourcelink = False
html_last_updated_fmt = '%Y年%m月%d日'

# 在 conf.py 末尾添加
# latex_engine = 'xelatex'
#
# latex_elements = {
#     'papersize': 'a4paper',
#     'pointsize': '11pt',
#     'fontpkg': r'''
# \setmainfont{SimSun}
# \setsansfont{SimHei}
# \setmonofont{Fira Mono}
# ''',
#     'babel': r'\usepackage[UTF8]{ctex}',
# }
