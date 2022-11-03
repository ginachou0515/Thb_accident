#Xlsx檔讀取輸出
#outputExcelCSV
import pandas as pd
import os



# 讀取excel檔
def ReadExcel(file, sheet= 0):
    return pd.read_excel(file, encoding="utf-8", sheet_name=sheet)

# 產出excel檔
def OutputExcel(dataframe,name,sheet = '工作表1'):
    Result_Path = './output/test'# 開啟檔案
    if not os.path.exists(Result_Path):
        os.makedirs(Result_Path)
    Result_Name = Result_Path + '/' + name +".xlsx"
    #excel_writer ： ExcelWriter目標路徑
    writer = pd.ExcelWriter(Result_Name)
    #writer = pd.ExcelWriter(Result_PATH, engine='xlsxwriter')
    dataframe.to_excel(writer, sheet_name=sheet, index=False, encoding='utf-8')
    writer.save()
    print('成功產出' + Result_Name)

# 判斷某欄位內包含某個字符串
def Filter(dataframe, colname, filter):
    # 進行字符串化，並得到其對應的布爾值：
    # 通過dataframe的基本操作將其選取出來:
    return dataframe[dataframe[colname].str.contains(filter)]
# 判斷某欄位內不包含某個字符串
def TransFilter(dataframe, colname, filter):
    return ~dataframe[dataframe[colname].str.contains(filter)]

if __name__ == '__main__':
    Path = './'
    Path = Path +'output'+'/'
    # def Read(Path = './', filename, sheet= 0):
    # 列出指定路徑底下所有檔案(包含資料夾)
    allFileList = os.listdir(Path)

    filename =input('輸入檔名:')
    # 逐一查詢檔案清單
    for file in allFileList:
        #   這邊也可以視情況，做檔案的操作(複製、讀取...等)
        #   使用isdir檢查是否為目錄
        #   使用join的方式把路徑與檔案名稱串起來(等同filePath+fileName)
        if os.path.isdir(os.path.join(Path, file)):
            print("I'm a directory: " + file)
        #   使用isfile判斷是否為檔案
        elif os.path.isfile(Path + file):
            print(f'資料名稱:{file}')
            if(file.find(filename)!=-1):#if(filename in file):
                print(f'資料\t{file}\t與輸入名稱\t{filename}相符')
                #print(f'當前工作目錄為:{os.getcwd()}')
                new = os.path.join(Path, file)
                print(f'新的工作目錄為:{new}')
                db = pd.read_excel(new)
        else:
            print('OH MY GOD !!')


## 與listdir不同的是，os.walk只是將指定路徑底下的目錄和檔案列出來

# # walk的方式則會將指定路徑底下所有的目錄與檔案都列出來(包含子目錄以及子目錄底下的檔案)
# allList = os.walk(Path)
# # 列出所有子目錄與子目錄底下所有的檔案
# for root, dirs, files in allList:
# #   列出目前讀取到的路徑
#   print("path：", root)
# #   列出在這個路徑下讀取到的資料夾(第一層讀完才會讀第二層)
#   print("directory：", dirs)
# #   列出在這個路徑下讀取到的所有檔案
#   print("file：", files)
#   for name in files:
#     print("filename：", os.path.join(root,name))#根目錄+子資料夾目錄+檔案名稱
#   # for name in dirs:
#   #   print("filepath：", os.path.join(root,name))#根目錄+子資料夾目錄



# file_name = "2017-2019年A1A2彙整.xlsx"
# accitype = ['A1','A2']
# year = [107, 108, 109]
# d1 = ReadExcel(file_name, f'{year[0]}年{accitype[0]}')
# d1 = d1.dropna(axis=0, how='any')
#
# #df.dropna(axis=0, how='any', inplace=True)
# # axis：0-行操作（默認），1-列操作
# # how：any-只要有空值就刪除（默認），all-全部為空值才刪除
# # inplace：False-返回新的數據集（默認），True-在原數據集上操作
# #subset非常有用，如果想刪除所有列A 空值所在行：
# #df.dropna(axis = 0, subset = ['A'] )

