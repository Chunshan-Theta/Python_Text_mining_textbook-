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
text5 = "    hello WORLD ;\n 哈摟 世界 ;\n 123 //(*´∀`)~♥   "
print(0,text5.split(' '))
print(1,[w for w in text5.split() if w.startswith('h')])
print(2,[w for w in text5.split() if w.endswith('D')])
print(3,[w for w in text5.split() if w.isalpha()])
print(4,[w for w in text5.split() if w.isdigit()])
print(5,[w for w in text5.split() if w.isalnum()])

print("\n")
print("-"*20,"6")
# text operation
print(1,text5.lower())
print(2,text5.upper())
print(3,text5.title())
print(4,text5.split(';'))
print(5,text5.splitlines())
print(6,'\n'.join(text5.splitlines()))
print(7,text5.strip().split(' '))






