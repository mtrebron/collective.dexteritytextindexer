from setuptools import setup, find_packages

version = '2.1.1'

tests_require = [
    'zope.configuration',
    'plone.testing',
    'plone.app.testing',
    'plone.autoform',
    ]

setup(name='collective.dexteritytextindexer',
      version=version,
      description="Dynamic SearchableText index for dexterity content types",

      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='plone dexterity searchable text indexer',
      author='Jonas Baumann',
      author_email='mailto:info@4teamwork.ch',
      url='http://github.com/collective/collective.dexteritytextindexer',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',

        'ZODB3',
        'zope.interface',
        'zope.schema',
        'zope.component',
        'zope.deferredimport',
        'z3c.form',

        'plone.indexer',
        'plone.behavior',
        'plone.dexterity',
        'plone.app.dexterity',
        'plone.supermodel >= 1.1.1',
        'plone.z3cform',
        'Products.CMFCore',
        ],

      tests_require=tests_require,
      extras_require=dict(
        tests=tests_require,
        namedfile=['plone.namedfile']),

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
