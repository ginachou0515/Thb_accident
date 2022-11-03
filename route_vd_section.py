#!/usr/bin/env python3.7?
# -*- coding: utf-8 -*-
import pandas as pd
import os
import openpyxl as opxl
# 資料存在與否
def file_exist_or_not(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return 0
# 讀取excel檔
def ReadExcel(file, sheet= 0):
    return pd.read_excel(file, encoding="utf-8", sheet_name=sheet)

# 產出excel檔
def OutputExcel(dataframe, outpath, name,sheet = '工作表1'):
    outname = f'{name}.xlsx'
    out_file = os.path.join(outpath, 'output')
    file_exist_or_not(out_file)
    data_file = os.path.join(out_file, outname)
    #excel_writer ： ExcelWriter目標路徑
    writer = pd.ExcelWriter(data_file)
    #writer = pd.ExcelWriter(Result_PATH, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name=sheet, index=False, encoding='utf-8')
    writer.save()
    print(f'成功產出{outname}')
    return 0

def output_to_csv(df, date, outpath, outputname):
    """
    :param xml_df:要輸出的dataframe資料
    :param outpath:資料輸出路徑
    :param date:日期名稱
    :param outputname :輸出檔名
    """
    section_file = os.path.join(outpath, outputname)
    df.to_csv(f'{section_file}_{date}.csv', index=None, encoding='utf_8_sig')
    print('Successfully converted to csv.')
    return 0



if __name__ == "__main__":
    path = os.getcwd()
    data_root = os.path.join(path, 'section')
    file_exist_or_not(data_root)
#     # excel_file = os.path.join(data_root, '西部快速公路設備_全設備對應路段.xlsx')
#     # confi = pd.read_excel(excel_file)
#     excel_file = os.path.join(data_root, '西部快速公路設備_對應路段.xlsx')
#     confi = pd.read_excel(excel_file,sheet_name='全設備')
# ###以上OK


    # section_file = os.path.join(data_root, '108年整理_ALL_平日_0909.xlsx')
    # route = '台61'
    # day_type = '平'  ##假
    # name = f'{route}({day_type})'
    # t61 = pd.read_excel(f'{section_file}', sheet_name=name)
    # t61f = opxl.load_workbook(f'{section_file}')
    # sheet = t61f.active
    #
    # for i in range(4, 20):
    #     # sheet['A{}'.format(i)] =
    #     cell = sheet[f'A{i}']
    #     print(cell.value)
    #     # cell.value =
# ###取值OK

        # for column in sheet['A:C']:
    #     for cell in column:
    #         print(cell.value)
    # # 操作多列
    # for column in t61['A:C']:
    #     for cell in column:
    #         print(cell.value)

    # opxl.workbook.save(filename="ALL_平日.xlsx")

    # OutputExcel(t61, data_root, name, sheet='工作表1')