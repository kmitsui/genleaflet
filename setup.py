# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='genleaflet',
    version='0.0.1',
    description='The genleaflet is a code generator of Leaflet by Python.',
    author='Ken-ichi Mitsui',
    author_email='datasetstream@gmail.com',
    license='MIT License',
    url='https://sites.google.com/site/datasetstream/genleaflet',
    keywords='data visualization',
    classifiers=['Development Status :: 4 - Beta',
                 'Programming Language :: Python :: 2.7',
                 'License :: OSI Approved :: MIT License'],
    packages=['genleaflet'],
    package_data={'': ['*.js',
                       'templates/html/*.html',
                       'templates/js/*.js',
                       'templates/ref/*.txt',
                       'templates/title/*.txt',
                       'templates/att/*.txt',
                       'plugins/*.js']}
)
