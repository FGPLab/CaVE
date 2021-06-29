# Qiime2 Plugin CaVE - Cell and Volume Estimator
## count-normalizer Plugin
---

 Plugin to get the relative volume and cell count based on predicted ribosomal counts.


# Installation
---
To install this plugin, clone or download this repo to your computer, activate your qiime environment, and then inside the directory/folder run:
```
python setup.py install
```
Once this plugin is installed, it gets added to your qiime distribution and is available every time you activate your qiime environment again. If you install a new version of qiime or have a new installation, you will have to reload the plugin.

Though, if the plugin installation doesn't work (i.e it installs and then proceeds to throw an error when you try to run it), you won't be able to use your qiime environment until you uninstall the program.


# Usage
---

There are some demo files included in the installation:

Inputs:
	--i-table {filename}: this is a qiime file with your OTU ID's and your sample's 16s amounts (Demo file: og.qza)
	--m-volumes-files {filename}: this is a metadata file with the feature id as one column, and the Volume count(average) as the 2nd column (Demo file: meta.tsv)

Outputs:
	--o-relcells {filename}   : this outputs the relative cell amounts normalized based on predicted ribosomal counts
	--o-relvolume {filename} :   this outputs the relative cell volumes normalized based on predicted ribosomal counts
	metadata.csv (natural output, always as this name): this output is a csv with the predicted ribosomal counts (rc) based on volume counts (vc)

```
cd demo
qiime CaVE count-normalize --i-table og.qza --m-volumes-file meta.tsv --o-relcells relcell.qza --o-relvolume relvol.qza
```

## Versions
---

2021 - Version 1 Released
