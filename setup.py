# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conda_vulnerability_scanner',
 'conda_vulnerability_scanner.resources',
 'conda_vulnerability_scanner.resources.binaries']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'conda-vulnerability-scanner',
    'version': '0.1.0',
    'description': 'Tool to scan for vulnerabilities in a conda environment.',
    'long_description': '###########################\nConda Vulnerability Scanner\n###########################\n\n********\nOverview\n********\n\nThis project allows you to scan a Conda Environment for Vulnerabilities.\nIt compares the installed packages to the `NVD NIST <https://nvd.nist.gov/>`_ database.\n\nDocumentation\n=============\n\n`Documentation for the current main branch <https://exasol.github.io/conda-vulnerability-scanner/main>`_ is hosted on the Github Pages of this project.\n`Here <https://exasol.github.io/conda-vulnerability-scanner>`_  is a list of documentations for previous releases.\n\nFeatures\n========\n\n* Compare conda packages against the NIST NVD database and report the CVEs',
    'author': 'Exasol AG',
    'author_email': 'opensource@exasol.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://exasol.github.io/conda-vulnerability-scanner/main/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
