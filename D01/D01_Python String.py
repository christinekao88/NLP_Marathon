all_review =\
'Wow... Loved this place.',\
'Crust is not good.',\
'Not tasty and the texture was just nasty.',\
'Stopped by during the late May bank holiday off Rick Steve recommendation and loved it.',\
'The selection on the menu was great and so were the prices.',\
'Now I am getting angry and I want my damn pho.',\
'Honeslty it didn\'t taste THAT fresh.)',\
'The potatoes were like rubber and you could tell they had been made up ahead of time being kept under a warmer.',\
'The fries were great too.'

pratice_sentence = all_review

# 字串長度
## format 用法之後會有詳細講解，這裡先了解會將後方字串放入{}即可
print('原始字串: {}'.format(pratice_sentence[0]))
## 運用len()得到字串長度
print('字串長度: {}'.format(len(pratice_sentence[0])))

# 取出特定區間文字
print('取出前五個字: {}'.format(pratice_sentence[0][:5]))
print('取出後五個字: {}'.format(pratice_sentence[0][-5:]))
print('取出後中間五個字: {}'.format(pratice_sentence[0][5:10]))

# 合併字串
print('原始字串1: {}'.format(all_review[0]))
print('原始字串2: {}'.format(all_review[1]))
##運用+符號可以直接合併兩字串
print(all_review[0]+all_review[1])
## 運用join function
print(''.join((all_review[0],all_review[1])))
## 加入separator
print('/'.join((all_review[0],all_review[1]),))

# 檢查字元是否在字串內
pratice_sentence = all_review[1]
print('原始字串: {}'.format(pratice_sentence))
print('is' in pratice_sentence)
print('I' in pratice_sentence)
print('I' not in pratice_sentence)

# strip() 用來移除頭尾的字元
pratice_sentence = all_review[1]
print('原始字串: {}'.format(pratice_sentence))
## 移除開頭
print(pratice_sentence.strip('Crust'))
## 移除尾部
print(pratice_sentence.strip('good.'))
## 由於is並不是開頭或結尾字符，因此返回原字串
print(pratice_sentence.strip('is'))
##移除開頭空格
print(' Crust is not good.'.strip())

# replace( ) 用來替換字元
pratice_sentence = all_review[2]
print('原始字串:   {}'.format(pratice_sentence))
## 用disgusting取代nasty
print(pratice_sentence.replace('nasty','disgusting'))
## 最多取代兩次
print(pratice_sentence.replace('t','T'))
print(pratice_sentence.replace('t','T',2))

# split( ) 用來切開字串
pratice_sentence = all_review[3]
print('原始字串:  {}'.format(pratice_sentence))
##用空格當分界隔開字串
print(pratice_sentence.split(' '))

# count() 用來計算字串內字元出現次數
pratice_sentence = all_review[4]
print('原始字串: {}'.format(pratice_sentence))
## 計算a出現次數
print(pratice_sentence.count('a')) ## == pratice_sentence.count('a',0,len(pratice_sentence))
##規定計算區間
print(pratice_sentence.count('a',2,10))

# startswith() / endswith() 用來判定字串頭尾是否為該字元
pratice_sentence = all_review[5]
print('原始字串:  {}'.format(pratice_sentence))
##檢查字串開頭是否為Now
print(pratice_sentence.startswith('Now'))
##檢查字串結尾是否為.
print(pratice_sentence.endswith('.'))
print(pratice_sentence.endswith('I'))

# capitalize() 會將字串開頭轉為大寫
##將開頭轉換為大寫
print('we love python'.capitalize())

# find() / index() 用來尋找字串中字元所在位置
# index() 不同於find()，當字元不存在時，會報錯，find() 則會返回 -1
pratice_sentence = all_review[6]
print('原始字串:  {}'.format(pratice_sentence))
## 尋找字串中 it 在哪
print(pratice_sentence.find('it')) ## == pratice_sentence.index('it')
print(pratice_sentence[9:9+len('it')])
## index與find功能，但找不到字元時會報錯，find會回報-1
# print(pratice_sentence.index('where'))
print(pratice_sentence.find('where'))

# upper() / lower() 會分別將整串字串轉換為大/小寫
pratice_sentence = all_review[7]
print('原始字串: {}'.format(pratice_sentence))
##全部轉換為大寫
print(pratice_sentence.upper())
##全部轉換為小寫
print(pratice_sentence.lower())

# Counter() 是一個相當方便的 function，可以快速計算字串中所有字元出現過的次數

from collections import Counter
##快速計算所有字元出現次數
count_ = Counter(all_review[8])
print(count_)
##出現最多的字元(前五名)
print(count_.most_common(5))
## 1 字元出現過幾次
print(count_.get('h'))