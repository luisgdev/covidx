""" Setup file """

import os

from setuptools import setup

from covidx import __app_name__, __version__


setup(
    name=__app_name__,
    version=__version__,
    description="Query Covid world records.",
    author="Luis Ch.",
    entry_points={
        "console_scripts": [
            f"{__app_name__} = {__app_name__}.__main__:main",
        ]
    },
)
