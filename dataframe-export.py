# !/usr/bin/env python
# coding=utf-8
# pylint: disable=C0111,C0330,C1801,W9006,R1260
"""
Python Script to write dataframe into csv/xlsx file to /tmp, specifically for small size data
"""

import pandas as pd
import pandas.io.formats.excel
import sys

def main(df, **kwargs):
    """
    This function is to transform dataframe to csv file or xlsx file which will be saved in /tmp/
    Usage: create_csv_or_xlsx_file(df,sep=None,file_name='data.xlsx',encoding='utf-8',create_xlsx_file=True,sheet_name='Overall')
    :param df: dataframe which needs to be transformed
    :arg string file_name: filename generated
    :arg string sheet_name: name of worksheet generated
    :arg boolean create_csv_file: if True, transform df into xlsx file; Otherwise, into csv file.
    :return nothing as this function is used to generate a file instead of returning any value
    """
    file_name = kwargs.get('file_name').lstrip("/")
    header = kwargs.get('header', True)
    if isinstance(header, basestring):
        header = header.upper() == 'TRUE'
    create_xlsx_file = kwargs.get('create_xlsx_file', False)
    if isinstance(create_xlsx_file, basestring):
        create_xlsx_file = create_xlsx_file.upper() == 'TRUE'
    sheet_name = kwargs.get('sheet_name', None)
    # set the name of worksheet which is "Sheet1" by default
    sheet_name = (sheet_name if sheet_name else "Sheet1")
    sep = kwargs.get('sep', "\t")
    encoding = kwargs.get('encoding', "UTF-8")
    if create_xlsx_file:
        # transform DataFrame df into xlsx file
        pandas.io.formats.excel.ExcelFormatter.header_style = None
        panda_df = df.toPandas()
        writer = pd.ExcelWriter("/tmp/" + file_name)
        panda_df.to_excel(
            writer,
            sheet_name=sheet_name,
            index=kwargs.get("index"),
            header=header,
            na_rep='',
            float_format=kwargs.get("float_format"),
            columns=kwargs.get('columns', None),
            index_label=kwargs.get("index_label"),
            startrow=kwargs.get('startrow', 0),
            startcol=kwargs.get('startcol', 0),
            engine=kwargs.get('engine', None),
            merge_cells=kwargs.get('merge_cells', None),
            encoding=encoding,
            verbose=kwargs.get('verbose', True),
            freeze_panes=kwargs.get('freeze_panes')
        )
        i = 0
        # to read .xlsx file more friendly
        # adjust column width in .xlsx file generated according to the max length of cell's content in this column
        for column_name, column_items in panda_df.items():
            column_width = max(column_items.astype(str).map(len).max(), len(str(column_name)) * 0.91) * 0.98
            worksheet = writer.sheets[sheet_name]
            worksheet.set_column(i, i, column_width)
            i += 1
        writer.save()
    else:
        # transform DataFrame df into csv file
        df.coalesce(1).toPandas().to_csv(
            sep=sep,
            header=header,
            index=kwargs.get("index", True),
            encoding=encoding,
            path_or_buf='/tmp/' + file_name,
            float_format=kwargs.get("float_format"),
            na_rep=kwargs.get('na_rep', ""),
            columns=kwargs.get("columns"),
            index_label=kwargs.get("index_label"),
            mode='w',
            compression='infer',
            quoting=kwargs.get("quoting"),
            quotechar=kwargs.get("quotechar", '"'),
            line_terminator=kwargs.get("line_terminator"),
            chunksize=kwargs.get("chunksize"),
            tupleize_cols=kwargs.get("tupleize_cols"),
            date_format=kwargs.get("date_format"),
            doublequote=kwargs.get("doublequote", True),
            escapechar=kwargs.get("escapechar"),
            decimal=kwargs.get("decimal", '.')
        )
    return

if __name__=='__main__':
    main(sys.argv[1], # df
         **dict(arg.split('=') for arg in sys.argv[2:])) # kwargs
