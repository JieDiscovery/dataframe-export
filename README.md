# Save Dataframe as .csv or .xlsx file
![GitHub](https://img.shields.io/github/license/JieSONG/BigData_Tools)
## Motivation
During big data development, sometimes we would like to save Dataframe(which might be achieved by SQL Query or somewhere else) into a specific file type 
such as .csv or .xlsx file to easily deliver it into other non-technical colleague or clients. So that they could simply open this file to read data and do data 
analysis on them using MS excel etc.

## Configuration
Download dataframe-export.py.

In your bash:
```bash
cd [to the folder contains dataframe-export.py]
pip install virtualenv
virtualenv env --python=python2.7
pip install -r requirements.txt

```

## Usage
In your bash:
```bash

python write_csv_or_xlsx_file(df, sep=',', header=True, file_name="app-discovery-2020.xlsx", encoding='utf-8', create_xlsx_file = True, sheet_name = "first_sheet")
```
Wait a couple seconds, the file generated from DataFrame will be saved in /tmp.


