# 以 jieba 進行斷詞，輸出為 generator，需要使用遞迴將值取出

import jieba

# 將結巴使用的字典更改為對繁體中文表現較好的字典
jieba.set_dictionary('/Users/kao_oak/Documents/GitHub/NLP_Marathon/jieba/extra_dict/dict.txt.big')

input_str = '小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造'
cutted_words = jieba.cut(input_str)
words = [word for word in cutted_words]
print(words)

# 辨識新字詞
# 啟用 HMM 已辨識新字詞 (預設 HMM 功能即為啟用，可以不用特地設為 True)
input_string = "他来到了网易杭研大厦"
cutted_words = jieba.cut(input_string, HMM=True)
words = [word for word in cutted_words]
print(words)

# 在既有使用的字典下新增自定義字詞
jieba.load_userdict("jieba/test/userdict.txt")

# 動態加入字典
jieba.add_word("國立臺灣大學")
# 動態調整詞頻
jieba.suggest_freq("國立臺灣大學", True)

# 進行詞性標注(PoS Tagging)

import jieba.posseg as pseg

input_str = "小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造"
cutted_words = pseg.cut(input_str)
words = [(word, flag) for (word, flag) in cutted_words]
print(words)

# 取出斷詞位置

input_str = u'小明碩士畢業於國立臺灣大學，現在在日本東京大學進修深造' #在此將字串轉為unicode
words = jieba.tokenize(input_str)
for tk in words:
    print(f'word:{tk[0]}, start:{tk[1]}, end:{tk[2]}')