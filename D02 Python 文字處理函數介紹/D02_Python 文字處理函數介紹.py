"""
判別字串是否為特定字元 :
string.isnumeric()，string.isdigit()，string.isdecimal()
三者皆是用來判定字串內是否都屬於數值字元，差別主要在於 unicode 定義的區間不同，
isdecimal() ⊆ isdigit() ⊆ isnumeric()
"""

# isalnum():如果 string 至少有一個字符和所有字符都是字母或數字則返回 True，否則返回 False。

print('23'.isalnum())

print('我要學python'.isalnum())

# .不算字母或數字
print('我要學python.'.isalnum())

# space 不算字母或數字
print('我要學python '.isalnum())

# isupper() / islower() : 判定字串內字元是否都為大寫/小寫

print('ABC'.isupper())
print('ABC'.islower())
print('ABc'.islower())

# String.format() : 以可讀性更高的語法做到 string formatting , 基本语法是通过 {} 和 : 来代替以前的 %
print('{} {} {}'.format('I','Love','Python'))
print('{1} {0} {2}'.format('Love','I','Python'))
print('{name} {verb} {language}'.format(verb = 'Love', name = 'I', language = 'Python'))

# 補齊數字字串長度

## > 補右邊, 補0到10位數
print('{:0>10d}'.format(5))

## > 補左邊, 補1到10位數
print('{:1>10d}'.format(5))

## > 補左邊, 補空格，可用來對齊
print('{:>10d}'.format(5))