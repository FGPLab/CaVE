# ----------------------------------------------------------------------------
# FGP Lab
#
# ----------------------------------------------------------------------------


from .normalize import count_normalize

from qiime2.plugin import (Plugin, Metadata, Str, List, Citations, Range, Int,
                           Bool, Properties)
import qiime2

from q2_types.feature_data import FeatureData, Taxonomy, Sequence
from q2_types.feature_table import FeatureTable, Frequency

PARAMETERS = {'metadata': Metadata, 'custom_axes': List[Str],
              'ignore_missing_samples': Bool}
PARAMETERS_DESC = {
    'metadata': 'The sample metadata.',
    'custom_axes': ('Numeric sample metadata columns that should be '),
    'ignore_missing_samples': ()
}


plugin = Plugin(
    name='CaVE',
    version=1,
    website='http://garcia-pichel.lab.asu.edu/labo/',
    package='q2-FGP',
    # citations=Citations.load('citations.bib', package='q2_FGP'),
    description=('A Plugin to get the relative volume and cell count based on predicted ribosomal counts.'),
    short_description='A plugin to get the relative volume and cell count based on predicted ribosomal counts.'
)



######################################################################
plugin.methods.register_function(
    function=count_normalize,
    inputs={
        'table': FeatureTable[Frequency]
    },
    parameters={'volumes': qiime2.plugin.Metadata,},
    outputs=[
            ('relcells', FeatureTable[Frequency]),
            ('relvolume', FeatureTable[Frequency])
                ],
    input_descriptions={
        'table': 'This is some table input.'},
    parameter_descriptions={
        'volumes' : ('A table that contains a column with the feature IDs and a column with the corresponding volume sizes of the features.')
    },
    output_descriptions={
        'relcells': 'A feature table that contains the relative number of cells and relative volume',
        'relvolume': 'A feature table that contains the relative number of cells and relative volume',
    },
    name='to get the relative volume and cell count based on predicted ribosomal counts.',
    description='A plugin to get the relative volume and cell count based on predicted ribosomal counts. '
)
######################################################################
