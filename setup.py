from setuptools import setup, find_packages

version = "0.1"

setup(name="tissue",
      version=version,
      description="Tissue - automated pep8 checker for nose",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords="",
      author="Jason K\xc3\xb6lker",
      author_email="jason@koelker.net",
      url="https://github.com/jkoelker/tissue",
      license="GNU LGPL",
      py_modules=["tissue"],
      install_requires=[
          "nose",
          "pep8",
      ],
      entry_points="""
      # -*- Entry points: -*-
[nose.plugins.0.10]
tissue = tissue:Tissue
      """,
      )