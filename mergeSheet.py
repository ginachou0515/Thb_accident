import pandas as pd
import xlrd
import os
#有合併的不能用
excel_name = '108交通量_東西向統整_平日.xlsx'
wb = xlrd.open_workbook(excel_name)
sheets = wb.sheet_names()
year = [107, 108]

# 讀取第一個sheets表格（此處不需要用到）
# df_10=pd.read_excel(excel_name,sheet_name=0,index=False,encoding='utf-8',columns=['content'])

##建立一個新的表格存放數據
df1 = pd.DataFrame(columns=['content'])

##for循環，append剩下的sheets數據到第一個sheets
for i in sheets:
    df = pd.read_excel(excel_name, sheet_name=i, index=False, encoding='utf-8', columns=['content'])
    df1 = df1.append(df)


def OutputExcel(dataframe, name, sheet='工作表1'):
    Result_Path = './output'  # 開啟檔案
    if not os.path.exists(Result_Path):
        os.makedirs(Result_Path)
    Result_Name = Result_Path + '/' + name + ".xlsx"
    # excel_writer ： ExcelWriter目標路徑
    writer = pd.ExcelWriter(Result_Name)
    # writer = pd.ExcelWriter(Result_PATH, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name=sheet, index=False, encoding='utf-8')
    writer.save()
    print('成功產出' + Result_Name)

OutputExcel(df1, f'{year[1]}年總和')


# # 計算經過數據清理後的 DataFrame 分別的列數與行數
# for s_name in xls.sheet_names:
#     nrow, ncol = vars()["df_"+s_name].shape
#     print('df_{} => row: {}, column: {}'.format(s_name, nrow, ncol))
#
# # combining multiple dataframes
# df = pd.DataFrame()
#
# for s_name in xls.sheet_names:
#     df = pd.concat([df, vars()["df_"+s_name]], ignore_index=True)
#     print('=== {} success to concat ==='.format("df_"+s_name))
