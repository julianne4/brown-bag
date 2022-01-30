#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

REQUIREMENTS_FILE_PATH = Path(__file__).parent / "requirements.txt"
VERSION_FILE_PATH = Path(__file__).parent / "VERSION"
README_FILE_PATH = Path(__file__).parent / "README.md"

with open(VERSION_FILE_PATH) as f:
    version = f.read().strip()

with open(README_FILE_PATH, "r", encoding="utf-8") as f:
    long_description = f.read()


def _get_requirements(filename="requirements.txt"):
    "Return a list of requirements, read from a requirements_dev.txt file."
    with open(filename) as f:
        req = f.readlines()
    return [r.strip() for r in req]


setup(
    name=r"brown-bag",
    version=version,
    description=r"This is a demo repo for our brownbag talk!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=r"Anna Opperman",
    author_email=r"anna@dataprophet.com",
    url=r"https://github.com/DataProphet/brown-bag",
    packages=find_packages(exclude=("*tests", )),
    install_requires=_get_requirements(REQUIREMENTS_FILE_PATH),
    python_requires=">=3.7.5",
)