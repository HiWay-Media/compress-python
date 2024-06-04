# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='compress-python',
    version='0.3.0',
    url='https://github.com/HiWay-Media/compress-python',
    license='The MIT License',
    author='Allan Nava',
    author_email='allan.nava@hiway.media',
    keywords='compress tangram hiway media',
    description='python-keycloak is a Python package providing access to the Compress API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['compress', 'compress.tests'],
    install_requires=['requests>=2.20.0',],
    tests_require=['httmock>=1.2.5'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Utilities'
    ]
)
