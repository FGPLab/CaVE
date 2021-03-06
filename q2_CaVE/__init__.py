# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from .normalize import count_normalize
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__all__ = ['plot', 'procrustes_plot', 'biplot', 'generic_plot']
