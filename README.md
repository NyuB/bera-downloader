# Bulletin d'Estimation du Risque d'Avalanche (BERA) utilities

## Usage

### From the python sources
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

### With the bera-dl executable
Executables for Windows (bera-dl.exe) and Linux (bera-dl) can be downloaded from the releases.
```
bera-dl <MASSIF> <yyyy> <mm> <dd> --output-name <filename.pdf>
```