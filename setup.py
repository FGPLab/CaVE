# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
import versioneer

setup(
    name="q2-CaVE",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Ferran Garcia Pichel, Luis Gonzalez, Nicholas Ho, Daniel Roush",
    author_email="nichola2@asu.edu",
    description="Plugin to get the relative volume and cell count based on predicted ribosomal counts.",
    license='Modified BSD License',
    url="http://garcia-pichel.lab.asu.edu/labo/",
    entry_points={
        'qiime2.plugins':
        ['q2-CaVE=q2_CaVE.plugin_setup:plugin']
    },
    package_data={'q2_CaVE': ['']},
    zip_safe=False,
)
