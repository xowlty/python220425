# demoStr.py

from codecs import StreamReader


strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p",7))

#숫자나 문자열로만 이루어졌으면 True
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

#공백 없애기
strData = "<<<< spam and ham >>>>"
result = strData.strip("<> ") #전처리
print(strData)
print(result)

#spam을 spam egg로 변경
result2 = result.replace("spam", "spam egg")
print(result2)
#빈칸만나면 자르라는 split() -> 구분자를 지정안하면 공백을 기준으로 자름
lst = result2.split()
print(lst)
print(":)".join(lst))

