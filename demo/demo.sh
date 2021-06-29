#!/bin/bash


### this is the demo command specified in the README

qiime CaVE count-normalize --i-table og.qza --m-volumes-file meta.tsv --o-relcells relcell.qza --o-relvolume relvol.qza
