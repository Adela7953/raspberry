# 2022-05-22 python network programming


## 문자열 구성 파악 함수
```
'123'.isdigit()   숫자 확인
'abcABC'.isalpha()문자 확인
'Ab122'.isalnum() 문자+숫자 확인
'AB'.isupper()    대문자 확인
'ab'.islower()    소문자 확인
' '.isspave()     공백 확인

str.upper()       대문자로 전환
str.lower()       소문자로 전환
str.swapcase()    대소무자 상호 변환
str.title()       단어의 첫 글자를 대문자로 변환

str = 'Python programming is easy!'
str.count('i')
2
>>> str.find('om')
-1
>>> str.find('on')
4
>>> str.rfind('sy')
24
>>> str.index('on')
4
>>> 

```
