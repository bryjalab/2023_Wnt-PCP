# Proximity interactomics identifies RAI14, EPHA2 and PHACTR4 as essential components of Wnt/planar cell polarity pathway in vertebrates.

## Authors
Kristína Gömöryová<sup>1†</sup>, Nikodém Zezula<sup>1†</sup>, Tomasz W. Radaszkiewicz<sup>1†^</sup>, Petra Paclíková<sup>1</sup>, Štěpán Čada<sup>1</sup>, Kateřina Hanáková<sup>2</sup>, Miroslav Micka<sup>1</sup>, David Potěšil<sup>2</sup>, Zbyněk Zdráhal<sup>2</sup>, and Vítězslav Bryja<sup>1,3*</sup>

**Affiliations**

<sup>1</sup> Department of Experimental Biology, Faculty of Science, Masaryk University, Brno, Czech Republic.

<sup>2</sup> Central European Institute of Technology (CEITEC), Brno, Czech Republic.

<sup>3</sup> Institute of Biophysics of the Czech Academy of Sciences, Brno, Czech Republic.

<sup>†</sup> Equal contribution

<sup>*</sup> Corresponding author: bryja@sci.muni.cz


This repository accompanies the above-mentioned manuscript and provides scripts to reproduce some of the manuscript figures (the ones created in R and Python).

## Reproducing the manuscript figures

**Deposition of raw data to PRIDE**

All raw data were deposited to the ProteomeXchange Consortium via PRIDE and can be accessed by identifier [PXD048685](https://www.ebi.ac.uk/pride/archive/projects/PXD048685) and [PXD048678](https://www.ebi.ac.uk/pride/archive/projects/PXD048678).

**Scripts to reproduce the individual figures**

Scripts are located within the `src` folder:

- 01_DEP-analysis.Rmd (*Suppl. Fig. 1F*, *Fig. 2A*)
- 02_PCP-interactome-description.Rmd (*Fig. 1C, Fig. 1D, Fig. 1E*, *Suppl. Fig. 1G*)
- 03_REPRINT-data-preparation.Rmd 
- 04-Dotplots.Rmd (*Fig. 2B*, *Suppl. Fig. 2A*, *Suppl. Fig. 2B*)
- 05_Clusters-humancellmap.Rmd (*Fig. 2C*)
- 06_miniTurboID.Rmd (*Fig. 4C*, *Fig. 4D*, *Suppl. Fig. 4C*, *Suppl. Fig. 4D*)
- 07_RosePlots_LevanesTest.py (*Fig. 3F*, *Fig. 3G*)

All analyses were performed using R version 4.3.1 on the platform x86_64-w64-mingw32/x64 (64-bit) and python 3.12 on the same platform.
