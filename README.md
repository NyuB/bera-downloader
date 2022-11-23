# Bulletin d'Estimation du Risque d'Avalanche (BERA) utilities

## Usage : retrieving a BERA

### Using the python sources
Install dependencies :
```
pip install -r requirements.txt
```
Run main.py :
```
py main.py <MASSIF> <yyyy> <mm> <dd> --output-name <filename.pdf>
```
MASSIF is a valid massif in capital letters (use --help to list all available massifs).
yyyy mm dd represents year, month and day of the desired BERA. 
output-name specifies the file to write the bera pdf to, it is optionnal and defaults to BERA.pdf

Example for the Belledonne's BERA for the 21st of November 2022:
```
py main.py BELLEDONNE 2022 11 21 --output-name BELLEDONNE.pdf
```

### Using the bera-dl executable
Executables for Windows (bera-dl.exe) and Linux (bera-dl) can be downloaded from the releases named "binary-release"
```
bera-dl <MASSIF> <yyyy> <mm> <dd> --output-name <filename.pdf>
```

### From the daily release
BERAS for a variety of massif are published daily (around 18h30 CET) as release artifacts. For a given ```<massif>``` on a given date ```<yyyy>-<mm>-<dd>```, the BERA pdf can be found at ```https://github.com/NyuB/bera-downloader/releases/download/bera-release-<yyyy>-<mm>-<dd>/<massif>-<yyyy>-<mm>-<dd>.pdf```

For example, to get the BERA of the Aravis' massif on the 23rd of November 2022:
```
curl https://github.com/NyuB/bera-downloader/releases/download/bera-release-2022-11-23/Arravis-2022-11-23.pdf
```
