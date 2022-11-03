import pandas as pd
import numpy as np
import os
import glob


# Folder_Path = os.path.abspath(os.getcwd()) + '/non_domestic'
Folder_Path = 'D:/Users/63522/Desktop/data/TDCS_M08A'+'/20200711'
csv_list = glob.glob(os.path.join(Folder_Path, "*.csv")) #查看同文件夾下的csv文件數

SaveFile_Path = os.path.sep.join([Folder_Path, 'result']) ##輸出資料處
if not os.path.exists(SaveFile_Path):
    os.makedirs(SaveFile_Path)

csv_all = (os.path.join(SaveFile_Path, "result.csv"))

print('共發現%s個CSV文件'% len(csv_list))
print('正在處理............')

#####合併有標題資料的csv####
# # 讀取第一個CSV文件并包含表頭
# df = pd.read_csv(os.path.join(Folder_Path, csv_list[0]))  # 編碼默認UTF-8，若亂碼自行更改
#
# # 將讀取的第一個CSV文件寫入合併後的文件保存
# df.to_csv(csv_all, index=False)
#
# # 循環遍歷列表中各個CSV文件名，並追加到合併後的文件
# for i in range(1, len(csv_list)):
#     df = pd.read_csv(os.path.join(Folder_Path, csv_list[i]))
#     df.to_csv(csv_all, encoding="utf_8_sig", index=False, header=False, mode='a+')#不含標題

#####合併無標題資料的csv####
# # 讀取第一個CSV文件並且不把第一行作列屬性
df = pd.read_csv(os.path.join(Folder_Path, csv_list[0]), header=None)  # 編碼默認UTF-8，若亂碼自行更改

# # 將讀取的第一個CSV文件，命明標題再寫入合併後的文件保存
df.columns = ['TimeInterval','GantryFrom','GantryTo','VehicleType','Traffic']
df.to_csv(csv_all, index=False)

# 循環遍歷列表中各個CSV文件名，並追加到合併後的文件
for i in range(1, len(csv_list)):
    df = pd.read_csv(os.path.join(Folder_Path, csv_list[i]), header=None)#不把第一行作列屬性
    df.to_csv(csv_all, index=False, header=False, mode='a+') #不含標題



print('合併完畢！')



##去重函數
##這個函數將重複的內容去掉，主要是去表頭。
#DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)