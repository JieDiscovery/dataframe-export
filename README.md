# Save Dataframe as .csv or .xlsx file
![GitHub](https://img.shields.io/github/license/JieDiscovery/dataframe-export)
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
[define the dataframe df firstly]
python dataframe-export.py df sep=[sep] header=[if_header] file_name=[file_name] encoding=[encoding] create_xlsx_file=[if_create_xlsx] sheet_name=[sheet_name] 

ex.
python dataframe-export.py df sep=',' header=True file_name='app-discovery-2020.xlsx' encoding='utf-8' create_xlsx_file = True sheet_name = 'Overall'
```
Wait a couple seconds, the file generated from DataFrame will be saved in /tmp.


