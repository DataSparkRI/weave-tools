from distutils.core import setup
setup(
    name = "django-weave_tools",
    packages = ["weave_tools"],
    version = "0.0",
    description = "Weave tools for Django",
    author = "The Providence Plan",
    author_email = "plandry@provplan.org",
    url = "https://github.com/ProvidencePlan/weave-tools/tree/master/django",
    download_url = "https://github.com/ProvidencePlan/weave-tools/tarball/master",
    keywords = ["weave", "visualization", "django"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        ],
    long_description = """\
Django tools for the Open Indicator Consortium's Weave visualization environment.

This app provides a simple Django model-based interface for the Weave visualization
system.
"""
)

