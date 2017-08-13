# Python3
# note by Theta
# 2017/8/13

print("\n")
print("-"*20,"1")
# The length of text1 and textA
# 打印出text1和textA的長度
text1 = "Ethics are built right into the ideals and objectives of the United Nations. "
textA = "倫理建立在聯合國的理想和目標之中"
print(len(text1),len(textA)) 


print("\n")
print("-"*20,"2")
# Return a list of the words in text2, separating by ' '.
# 回傳一個 text2的文字列表,利用' '來做區隔
# 中文詞之間並沒有空格,所以不會被分詞
text2 = text1.split(' ')
textB = textA.split(' ') 
print(len(text2),text2)
print(len(textB),textB)


print("\n")
print("-"*20,"3")
# Words that are greater than 3 letters long in text2
# Capitalized words in text2
# Words in text2 that end in 's'
# 打印出text2中長度大於3個字母的單詞
# 打印出text2中大寫字母開頭的單詞
# 打印出在text2中以's'結尾的單詞
print([w for w in text2 if len(w) > 3])
print([w for w in text2 if w.istitle()]) 
print([w for w in text2 if w.endswith('s')]) 


print("\n")
print("-"*20,"4")
# Get unique words in text4
# len(set(text4)) would gat 5 because the first word is Capitalized
# so to fix that we should lowercase the text
# 取出text4中不重複之詞彙
# len(set(text4)) 將會得到長度是5,因為第一個字是大寫
# 為了修補這個錯誤,我們應該要把文字全部改成小寫
text3 = 'To be or not to be'
text4 = text3.split(' ')
print(len(text4),text4)
print(len(set(text4)),set(text4))
print(len(set([w.lower() for w in text4])),set([w.lower() for w in text4]))


print("\n")
print("-"*20,"5")
# some word comparison function
#1/ start with 'h'
#2/ end with 'D'
#3/ is alphanumeric (No number,No apace,No punctuation marks)
#4/ is number (only numbers)
#5/ is alphanumeric or number (No apace,No punctuation marks)
# 一些文字比對的方法
#1/ 開頭為'h'
#2/ 結尾為'D'
#3/ 是不是文字
#4/ 是不是數字
#5/ 是不是數字或文字
text5 = "    hello WORLD ;\n 哈摟 世界 ;\n 123 //(*´∀`)~♥ hello WORLD  "
print(0,text5.split(' '))
print(1,[w for w in text5.split() if w.startswith('h')])
print(2,[w for w in text5.split() if w.endswith('D')])
print(3,[w for w in text5.split() if w.isalpha()])
print(4,[w for w in text5.split() if w.isdigit()])
print(5,[w for w in text5.split() if w.isalnum()])


print("\n")
print("-"*20,"6")
# some text operation function
#1/ All lowercase
#2/ All capitalized
#3/ All titlecase
#4/ Return a list of the words in text5, separating by ';'
#5/ Return a list of the words in text5, separating by '\n'
#6/ Return a list of the words in text2, combined with '~'
#7/ Remove space from sentence begin and end
#8/ search 'WORLD'" from the start of sentence
#9/ search 'WORLD' from the end of sentence
#A/ search ALL 'WORLD' and replace to 'Python'
# 一些文字操作方法
#1/ 全部小寫
#2/ 全部大寫
#3/ 字開頭大寫
#4/ 利用';'來分隔成陣列
#5/ 利用跳行來分隔成陣列
#6/ 利用'~'將陣列元素組成句子
#7/ 使用.strip()來去除句中前後不必要的空白與tab
#8/ (從句子前方開始)搜尋"WORLD"
#9/ (從句子後方開始)搜尋"WORLD"
#A/ 從句子中搜尋"WORLD"後改成'Python'
print(1,text5.lower())
print(2,text5.upper())
print(3,text5.title())
print(4,text5.split(';'))
print(5,text5.splitlines())
print(6,'~'.join(text5.splitlines()))
print(7,text5.strip().split(' '))
print(8,text5.find('WORLD'))
print(9,text5.rfind('WORLD'))
print('A',text5.replace('WORLD','Python'))


print("\n")
print("-"*20,"7")
# some text file operation function
#1/ open file named 'Your_File_.txt' with reading model
#2/ read the first of string from 'Demo.txt'
#3/ set searching point to the begin of the content
#4/ print number of word in file
#5/ print all sentence in file
#6/ close file
#7/ check the file is closed or not
# 一些檔案操作的方法
#1/ 以閱讀模式打開名叫 'Your_File_.txt' 
#2/ 讀取'Your_File_.txt'中第一個句子
#3/ 設置搜尋點在內容最前方
#4/ 打印出檔案中有多少個字
#5/ 打印出檔案中全部的句子
#6/ 關閉檔案
#7/ 確定膽案是否關閉
f = open("Your_File_.txt","r")
print(f.readlines())
f.seek(0)
print(len(f.read()))
print([s for s in f.splitlines()])
f.close()
f.closed()
