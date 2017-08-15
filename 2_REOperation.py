text1 = '"Ethics are built right into the ideals and objectives of the United Nations" \
#UNSG @ NY Society for Ethical Culture bit.ly/2guVelr @UN @UN_Woman @聯合國 @123Town @;[]#$%123 @こくさいれんごう'

#Find hashtag
#Find callouts
#找出井字號
#找出標記
print(1.1,[w for w in text1.split(" ") if w.startswith("#")])
print(1.2,[w for w in text1.split(" ") if w.startswith("@")])
print('='*20+'\n')




#import lib of regular expression
#Meta-characters: Character symbols
#\d : Any digit,equivalent [0-9]
#\D : Any non-digit,equivalent [^0-9]
#\s : Any whitespace, equivalent [ \t\n\r\f\v]
#\S : Any non-whitespace, equivalent [^ \t\n\r\f\v]
#\w : Any non-character symbols
#\W : Any character symbols
#+ : match once or more 
#* : match zero or more
#? : match Zero or once
#導入套件:regular expression
#Meta-characters: Character symbols
#\d : 任何數字,如同 [0-9]
#\D : 任何數字除外,如同 [^0-9]
#\s : 任何空白字元, 如同 [ \t\n\r\f\v]
#\S : 任何空白字元除外, 如同 [^ \t\n\r\f\v]
#\w : 任何標號字元除外
#\W : 任何標號字元
#+ : 符合一次以上 
#* : 沒有符合或符合一次以上
#? : 沒有符合或符合一次
import re
print(2.1,[w for w in text1.split(" ") if re.search('@\D+',w)])
print(2.2,[w for w in text1.split(" ") if re.search('@[A-Za-z0-9]+',w)])
print(2.3,[w for w in text1.split(" ") if re.search('@\w+',w)])
print(2.4,[w for w in text1.split(" ") if re.search('@[^A-Za-z0-9;]+',w)])
print('='*20+'\n')




#Finding Specific character
#Find 'a','e','i','o','u' in text2
#Find character that are not 'a','e','i','o','u' in text2
#找到指定字元
#找到text2中的'a','e','i','o','u'字元
#找到text2中'a','e','i','o','u'以外的字元

text2 = 'pneumonoultramicroscopicsilicovolcanoconiosis'
print(3.1,re.findall('[aeiou]',text2))
print(3.2,re.findall('[^aeiou]',text2))
print('='*20+'\n')




#Regular Expression for Dates
#{n} :exactly n repetitions,n>=0
#{n,}:at least n repetitions
#{,n}:at most n repetitions
#{n,m}: at least m and at most n repetitions
#正式日期處理
#{n} :有n個
#{n,}:最少有n個
#{,n}:最少多n個
#{n,m}: 最少又n個且最多又m個
text3 = '\n23-10-2002\n23/10/2002\n23/10/02\n10/23/2002\n23 Oct 2002\n23 October 2002\nOct 23, 2002\nOctorber 23, 2002'
print(4.1,text3)
print(4.2,re.findall('\d{1,2}[-/]\d{1,2}[-/]\d{4}',text3))
print(4.3,re.findall('\d{1,2}[-/]\d{2}[-/]\d{2,4}',text3))
print(4.4,re.findall('\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{4}',text3))
print(4.5,re.findall('\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}',text3))
print(4.6,re.findall('(?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{1,2}, )?\d{2,4}',text3))

