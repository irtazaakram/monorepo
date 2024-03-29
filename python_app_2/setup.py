#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Irtaza Akram",
    author_email='irtaza.akram@arbisoft.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Example python app for testing",
    entry_points={
        'console_scripts': [
            'python_app_2=python_app_2.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords='python_app_2',
    name='python_app_2',
    packages=find_packages(include=['python_app_2', 'python_app_2.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/irtazaakram/python_app_2',
    version='0.1.0',
    zip_safe=False,
)
