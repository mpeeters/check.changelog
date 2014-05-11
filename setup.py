from setuptools import setup
from setuptools import find_packages

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(name='check.changelog',
      version=version,
      description="Check changelog from packages",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='Martin Peeters',
      author_email='martin.peeters@affinitic.be',
      url='https://github.com/mpeeters/check.changelog',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['check'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'docutils',
          'setuptools',
          'zest.releaser',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'console_scripts': [
              'check-changelog = check.changelog.script:main',
          ]
      })
