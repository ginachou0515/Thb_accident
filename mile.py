#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re  # 調用re庫

# 要搜尋的內文
text = "台61線 172公里100公尺"
text2 ='嘉義縣布袋鎮台61線 快速道路北上279公里北'
text3 ='布袋鎮台61線平面道路南下126K'
text4 ='布袋鎮台61線124k'
text5 = '桃園市大園區台61線南向31.7K'

place =['桃園市大園區台61線 31公里600.0公尺處南向內側',
'苗栗縣後龍鎮海寶里台61線北上慢車道95.4公里附近',
'彰化縣線西鄉台61線 169公里800.0公尺處北側向內側',
'嘉義縣東石鄉台61線263K北向東石交流道口',
'彰化縣伸港鄉台61線 169公里北側向中外',
'彰化縣鹿港鎮台61線 172公里100.0公尺處北側向外側',
'雲林縣麥寮鄉台61線 216.1公里100.0公尺處北向外側'

]



p1 = [".*?台61線.*?(\d+)K", ".*?台61線.*?(\d+)k"]
pk = '|'.join(p1)#將想過濾的「表達式」變成一表達規則
pd = re.compile(pk)

###
pint1 = [".*?台61.*?(\d+)公里(\d+)公尺", ".*?台61.*?(\d+)公里",".*?台61.*?(\d+)公尺",
         ".*?臺61.*?(\d+)公里(\d+)公尺", ".*?臺61.*?(\d+)公里", ".*?臺61.*?(\d+)公尺"]
pint2 = [".*?台61.*?(\d+)K", ".*?台61.*?(\d+)k",
         ".*?臺61.*?(\d+)k", ".*?臺61.*?(\d+)k"]
pfloat1 =[".*?台61.*?(\d\d\d\.\d+)公里(\d\d\d\.\d+)公尺", ".*?台61.*?(\d\d\d\.\d+)公里",".*?臺61.*?(\d\d\d\.\d+)公里(\d\d\d\.\d+)公尺", ".*?臺61.*?(\d\d\d\.\d+)公里"]
pfloat2 =[".*?台61.*?(\d\d\d\.\d+)K", ".*?台61.*?(\d\d\d\.\d+)k", ".*?臺61.*?( \d\d\d\.\d+)k", ".*?臺61.*?(\d\d\d\.\d+)k"]

#往下減少百位數 以及還有整數與浮點數的組合





#pattern =[]

# 第一個參數代表 pattern，後者代表內文
match_objectA1 = re.search(".*?台61.*?(\d+)公里(\d+)公尺", text)
match_objectA2 = re.search(".*?台61.*?(\d+)公里", text)
match_objectB1 = re.search(".*?台61.*?(\d+)公里(\d+)公尺", text2)
match_objectB2 = re.search(".*?台61.*?(\d+)公里", text2)
match_objectC1 = re.search('.*?台61線.*?(\d+)K', text3)
#match_objectD1 = re.search('.*?台61線.*?(\d+)K|.*?台61線.*?(\d+)k', text4)
match_objectD1 = re.search(pd, text4)
match_objectE1 = re.search('.*?台61線.*?(\d\d\.\d+)K|.*?台61線.*?(\d\d\.\d+)k', text5)

#result = re.search('Hello.*?(\d+).*?Demo', content)
# comment = re.compile(r"台61.*(\d+)公里(\d+)公尺")
# num = comment.findall(text)
# print(num)

# 如果要抓到，就會回傳一個 Match Object，若無則回傳 None
if match_objectA1:
    # group 函式會回傳截取的內容，0 代表自己， 1 代表第一個截
    # 取的內容，依此類推
    print("A1")
    #print(match_objectA1)#[('172', '100')]
    print(match_objectA1.group())  # 台61線 172公里100公尺
    print(match_objectA1.group(1))  # 172
    print(match_objectA1.group(2))  # 100
else:
    print('A1沒找到符合資料')
if match_objectA2:
    # group 函式會回傳截取的內容，0 代表自己， 1 代表第一個截
    # 取的內容，依此類推
    print("A2")
    print(match_objectA2.group(0))  # '台61線 172公里'
    print(match_objectA2.group(1))  # 172
else:
    print('A2沒找到符合資料')
if match_objectB1:
    print("B1")
    print(match_objectB1.group(0))  # ''
    print(match_objectB1.group(1))  #
else:
    print('B1沒找到符合資料')
if match_objectB2:
    print("B2")
    print(match_objectB2.group())  # '嘉義縣布袋鎮台61線 279公里'
    print(match_objectB2.group(1))  # 279
else:
    print('B2沒找到符合資料')

if match_objectC1:
    print("C1")
    print(match_objectC1.group())  # '布袋鎮台61線126K'
    print(match_objectC1.group(1))  # 126
else:
    print('C1沒找到符合資料')

if match_objectD1:
    print("D1")
    #Match.lastindex
    #捕獲組的最後一個匹配的整數索引值，或者 None
    #如果沒有匹配產生的話。比如，對於字符串 'ab'，表達式 (a)b, ((a)(b)), 和 ((ab)) 將得到 lastindex == 1 ， 而 (a)(b) 會得到 lastindex == 2 。
    for i in range(match_objectD1.lastindex+1):
        print(match_objectD1.group(i))
else:
    print('D沒找到符合資料')

if match_objectE1:
    print("E1")
    print(match_objectE1.group())  # '布袋鎮台61線124k'
    print(match_objectE1.group(1))  # None
    print(match_objectE1.group(2))  # 124
    #print(match_objectE1.group(3))
else:
    print('E沒找到符合資料')

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
# if result:
#     # group 函式會回傳截取的內容，0 代表自己， 1 代表第一個截
#     # 取的內容，依此類推
#     print(result.group(0))  # 'Hello 1234567 World_This is a Regex Demo'
#     print(result.group(1))  # 1234567



# KM = re.findall('[KM,公里,k]', str)
# KM2 = re.findall('[KM,公里,k]', str2)
# KM3 = re.findall('[KM,公里,k]', str3)
# print(KM)
# print(KM2)
# print(KM3)

#我們回到之前電子郵件地址匹配的正則表達式，現在可以理解下列的意思:我們需要⼀個或者多個數字或字母（\w+） 後跟 at 符號（@），然後接⼀個或者多個數字或字母（\w+），跟著⼀個句號（.，注意這裡需要⼀個反斜槓轉 義），最後跟恰好三個⼩寫字母（[a-z]{3}）。
#email = re.findall(r'\w+@\w+\.[a-z]{3}')

