"""
Battery Data Processing Package

This package provides tools for processing and analyzing battery data.

Attributes:
    name (str): The name of the package.
    description (str): The description of the package
    author (str): The name of the author
    version (str): The version of the package.
    packages (list): A list of package modules.
    install_requires (list): Required dependencies for the package.

Note:
    This package requires Python 3.7 or later.

Example:
    To use this package, import it and its modules:

    >>> import pybatterydataproc
    >>> from pybatterydataproc import data_processing_module

    Then you can use functions and classes from the package.

"""

from setuptools import setup, find_packages

setup(
    name="pybatterydataproc",
    description='Your package description',
    author='Alexandru Pascu, part of the pybamm-param team from WMG',
    packages=['modules', 'classes', 'utils'],
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "chardet>=4.0.0",
        "openpyxl>=3.0.0",
        "plotly>=5.0.0",
        "pyarrow>=12.0.1"
    ],
)
