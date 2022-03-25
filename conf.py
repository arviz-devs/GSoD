project = "GSoD at ArviZ"
author = "ArviZ contributors"
copyright = f"2022, {author}"

version = ""
release = version

# -- General configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx_copybutton",
    "myst_parser",
    "sphinx_design",
]

exclude_patterns = [
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
    "README.md",
]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "code"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

extlinks = {
    "issue": ("https://github.com/arviz-devs/GSoD/issues/%s", "GH#"),
    "pull": ("https://github.com/arviz-devs/GSoD/pull/%s", "PR#"),
}

# -- Options for extensions

myst_enable_extensions = ["colon_fence", "deflist"]

# -- Options for HTML output

html_theme = "furo"
logo = "ArviZ.png"
html_static_path = ["sphinx"]
html_favicon = "sphinx/favicon.ico"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0f718e",
        "color-brand-content": "#069fac",
    },
    "dark_css_variables": {
        "color-brand-primary": "#069fac",
        "color-brand-content": "#00c0bf",
    },
    "sidebar_hide_name": True,
    "light_logo": logo,
    "dark_logo": f"dark-{logo}",
}

intersphinx_mapping = {
    "arviz": ("https://arviz-devs.github.io/arviz", None),
}
