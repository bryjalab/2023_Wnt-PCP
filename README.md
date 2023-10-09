# 2023_Wnt-PCP

Repository related to the Wnt/PCP interactome manuscript.

The structure of the repository is as follows:

- `data` folder contains all proteomic datasets (in a 'raw' form) used in the study
- `src` folder contains scripts which can be used to reproduce the analyses
- `outputs` folder contains the figures and tables generated while analyses

All raw data can be found in the PRIDE repository under identifier xxx.

The figures from manuscript can be reproduced using following scripts:

- `01_DEP-processing.Rmd`: analysis of proteinGroups.txt table using the [DEP](https://www.bioconductor.org/packages/release/bioc/html/DEP.html) R package (*Fig. 2A, Suppl. Fig. 1F*)
- `02_PCP-interactome-description.Rmd`: general description of interactome of individual baits (*Fig. 1C, 1C, 1E, Suppl. Fig. 1H*)
- `03_REPRINT-data-preparation.Rmd`: formats the input data (MS/MS counts) to format compatible with [REPRINT](https://reprint-apms.org/) tool
- `03_REPRINT-data-preparation.Rmd`: