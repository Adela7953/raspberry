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

str.strip()   양쪽에서 공백제거
str           원래 문자열은 변화X
str.rstrip()  오른쪽 공백제거
strlstrip()   왼쪽 공백제거

>>>s= 'a b' a와 사이에 공백이 있다
>>>s.split() s.split(None)와 같음
['a','b']
>>>str='abc'
>>>str.split('b') 문자열을 ()속의 문자로 분리
['a','c']
>>>'*'.join('hello') *와 문자열의 각 문자를 하나씩 결합한 문자열 생성
'h*e*l*l*o'

>>> str = 'abc'
>>> str.center(10)
'   abc    '
>>> str.center(10,'-')
'---abc----'
>>> 'he'.rjust(5) 5자리를 오른쪽으로 정렬
'   he'
>>> 'he'.ljust(5) 5자리를 왼쪽으로 정렬
'he   '
>>> 'he'.center(5) 5자리를 가운데로 정렬
'  he '
>>> '12'.zfill(5) 문자열 '12'의 왼쪽을 0으로 채워 5자리를 만든다다
'00012'
```
