'''Exercise 14) Write a Python program to combine two dictionary adding
values for common keys. '''

answer = {}

Dic1 = {'a': 100, 'b': 200, 'c': 300}
Dic2 = {'a': 200, 'b': 100, 'd': 400}

for i in Dic1.keys() :
    if i in Dic2 :
        ans = Dic1[i] + Dic2[i]
        answer[i] = ans # 파이썬 dictionary 추가 방법

print(answer)
        
    