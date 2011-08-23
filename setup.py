from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='Thingbox',
      version=version,
      description="Synchonisation of Tasks between Things and Teambox",
      long_description="""\
""",
      classifiers=[], 
      keywords='',
      author='Will Wheatley',
      author_email='will@iwill.id.au',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "appscript>1",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
