#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages
from setuptools import setup


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["derex.runner"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    author="Chiruzzi Marco",
    author_email="chiruzzi.marco@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"derex.runner": ["demo=derex.demo:config"]},
    description="Demo plugin for derex.runner",
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    dependency_links=[
        "http://github.com/Abstract-Tech/derex.runner/tarball/project-structure-and-readability#egg=derex.runner"
    ],
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="derex.demo",
    name="derex.demo",
    packages=find_packages(include=["derex.demo"]),
    namespace_packages=["derex"],
    test_suite="tests",
    url="https://github.com/Abstract-Tech/derex.demo",
    version="0.0.1",
    zip_safe=False,
)
