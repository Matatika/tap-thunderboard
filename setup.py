#!/usr/bin/env python
from setuptools import setup,find_packages

test_deps = [
    'pytest',
    'pylint',
    "mock",
]

extras = {
    'test': test_deps,
}

setup(
    name="tap-thunderboard",
    version="0.1.0",
    description="Collects data from Silicon Labs Thunderboard and outputs Singer messages to stdout.",
    author="aphethean",
    url="https://github.com/aphethean1/thunderboard-data",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_thunderboard"],
    install_requires=[
        "singer-python>=5.0.12",
        "bluepy>=1.3.0",
    ],
    tests_require=test_deps,
    extras_require=extras,
    entry_points="""
    [console_scripts]
    tap-thunderboard=tap_thunderboard:main
    """,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data = {
        "schemas": ["tap_thunderboard/schemas/*.json"]
    },
    include_package_data=True,
)
