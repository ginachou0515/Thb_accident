import pandas as pd
import numpy as np
import os
import sys

# 讀取excel檔
def ReadExcel(file, sheet= 0):
    return pd.read_excel(file, encoding="utf-8", sheet_name=sheet)

# 產出excel檔
def OutputExcel(dataframe,name,sheet = '工作表1'):
    Result_Path = './output'# 開啟檔案
    if not os.path.exists(Result_Path):
        os.makedirs(Result_Path)
    Result_Name = Result_Path + '/' + name +".xlsx"
    #excel_writer ： ExcelWriter目標路徑
    writer = pd.ExcelWriter(Result_Name)
    #writer = pd.ExcelWriter(Result_PATH, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name=sheet, index=False, encoding='utf-8')
    writer.save()
    print('成功產出' + Result_Name)
    # columns參數用於指定生成的excel中列的順序
    # sum_table.to_excel(writer, columns=['char','num'], index=False,encoding='utf-8',sheet_name='Sheet')
    # header :指定作為列名的行，預設0，即取第一行，資料為列名行以下的資料；若資料不含列名，則設定 header = None；
    # index：預設為True，顯示index，當index=False 則不顯示行索引（名字）

# 判斷發生地點大約位置
def Location(dataframe, filter):
    # 進行字符串化，並得到其對應的布爾值：
    # 通過dataframe的基本操作將其選取出來:
    return dataframe[dataframe['發生地點'].str.contains(filter)]
#不要忘記正則表達式的寫法，'.'在裡面要用'\.'表示

#(一)讀入資料
file_name = "107-108年A1A2彙整.xlsx"

year = [107, 108]
accitype = ['A1','A2']
d1 = ReadExcel(file_name, f'{year[0]}年{accitype[0]}')
d2 = ReadExcel(file_name, f'{year[0]}年{accitype[1]}')
d3 = ReadExcel(file_name, f'{year[1]}年{accitype[0]}')
d4 = ReadExcel(file_name, f'{year[1]}年{accitype[1]}')
print(d1.head(10))

sum_table = pd.concat([d1, d2, d3, d4], axis=0, ignore_index=True)
# #concat縱向合併，並將index_ignore設定為True
# res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
# #合併多個df，將df2與df3合併至df1的下面，以及重置index，並打印出結果
# res = df1.append([df2, df3], ignore_index=True)

#刪除有NaN的行
sum_table = sum_table.dropna(axis=0, how='any')


#(2)['台61','東西快','台62甲','台65']
WestExpressway = ['台61','東西快','台62甲','台65']

T61 = ['台61','臺61']
E0 = '|'.join(T61)
EastWestExpressway =['台62','台64','台66','台68',
                     '台72','台74','台76','台78',
                     '台82','台84','台86','台88',
                     '臺62','臺64','臺66','臺68',
                     '臺72','臺74','臺76','臺78',
                     '臺82','臺84','臺86','臺88']
E1 = '|'.join(EastWestExpressway)
T62A = ['台62甲','臺62甲']
E2 = '|'.join(T62A)
T65 = ['台65','臺65']
E3 = '|'.join(T65)

#['台61']
filter1 = Location(sum_table, E0)
OutputExcel(filter1, f'{year[0]}-{year[-1]}年A1A2總和_{WestExpressway[0]}')
#['東西快']
filter2 = Location(sum_table, E1)
OutputExcel(filter2, f'{year[0]}-{year[-1]}年A1A2總和_{WestExpressway[1]}')
#['台62甲']
filter3 = Location(sum_table, E2)
OutputExcel(filter3, f'{year[0]}-{year[-1]}年A1A2總和_{WestExpressway[2]}')
#['台65']
filter4 = Location(sum_table, E3)
OutputExcel(filter4, f'{year[0]}-{year[-1]}年A1A2總和_{WestExpressway[3]}')

#(1)總和
OutputExcel(sum_table, f'{year[0]}-{year[-1]}年A1A2總和')

#整型數字：目標sheet所在的位置，以0為起始，比如sheet_name = 1代表第2個工作表。
# timedf = pd.read_excel(tfile_name, encoding ="utf-8", sheet_name = 0)
# timedf2 = pd.read_excel(tfile_name, encoding ="utf-8", sheet_name = 1)
#列表名：目標sheet的名稱，中英文皆可。
# timedf = pd.read_excel(file_name, encoding ="utf-8", sheet_name = '一到三車道')
# timedf2 = pd.read_excel(file_name, encoding ="utf-8", sheet_name = '匝環道')

