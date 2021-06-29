# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
# Modified By Nicholas Ho in FGP Lab
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources
import pandas as pd

import qiime2
import q2templates
import numpy as np



def calc(vc):
    estimated_rc = 7.25 * (vc ** (2/3))
    return float(estimated_rc.real)

def get_vc(species, meta_data):
    if(len(meta_data[meta_data.index == species]) != 0):
        vc_col = meta_data.columns[0]
        vc = meta_data[meta_data.index == species][vc_col][0]
        return float(vc)
    else:
        print('no vc found for: ', species)
        return -1 ## this helps find and filter out the ones that have no volume counts

def divide(x,y):
    return x/y

def mult(x,y):
    return x*y



def count_normalize(table: pd.DataFrame, volumes: qiime2.Metadata) -> (pd.DataFrame,pd.DataFrame) :
    df = table.transpose()
    meta_data = volumes.to_dataframe()
    # list_of_samples = list(df.columns[1:])
    list_of_samples = list(df.columns)

    list_vc = []
    print(df)
    print(meta_data)
    for i in range(len(df)):
        # species = df.iloc[i]['feature id']
        species = df.index[i]
        print(species)
        list_vc.append(get_vc(species.strip(), meta_data))

## this adds two new columns used for calculations, the volumn counts (from the )
    df['vc'] = list_vc
    df['calculated_rc'] = df['vc'].apply(calc)

    df = df[df['vc'] >= 0]


    for curr in range(len(list_of_samples)):
        df['rel_to_total_phototrophs-' + list_of_samples[curr]] = df[list_of_samples[curr]] / df[list_of_samples[curr]].sum()
        df['H-' + list_of_samples[curr]] = divide(df['rel_to_total_phototrophs-' + list_of_samples[curr]], df['calculated_rc'])
        df['rel_number_of_cells-' + list_of_samples[curr]] = df['H-' + list_of_samples[curr]] / df['H-' + list_of_samples[curr]].sum()
        df['J-' + list_of_samples[curr]] = mult(df['rel_number_of_cells-' + list_of_samples[curr]], df['vc'])
        df['relative_volume-' + list_of_samples[curr]] = df['J-' + list_of_samples[curr]]/df['J-' + list_of_samples[curr]].sum()

    print(df)
    list_to_keep = []
    # list_to_keep = ['feature id']

    list_to_keep = list_to_keep + list_of_samples
    list_to_keep.append('vc')
    list_to_keep.append('calculated_rc')

    vc_cols = ['vc', 'calculated_rc']
    relative_cells = []
    relative_volume = []

    for sample in list_of_samples:
        list_to_keep.append('rel_number_of_cells-' + sample)
        list_to_keep.append('relative_volume-' + sample)

        relative_cells.append('rel_number_of_cells-' + sample)
        relative_volume.append('relative_volume-' + sample)


    out1 = df[relative_cells]
    out1.columns = list_of_samples
    out2 = df[relative_volume]
    out2.columns = list_of_samples
    out3 = df[vc_cols]

    out3.index.name = "#OTU ID"
    out3.to_csv('metadata.csv')

    return out1.transpose(), out2.transpose() #, out3.transpose()

    # mass_df = masses.to_dataframe()
    #table.view(pd.DataFrame)[:level]
    # return table.iloc[:level]
    # return mass_df
