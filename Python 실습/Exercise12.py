'''Exercise 12) Write a Python program to add members in a set
{“Monday”,”Tuesday”,”Wednesday”,”Thursday”,”Friday”}. Note adding
string in Python means concatenating strings.'''

week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
day = []
day.append(input())
week.update(day) #week에 day에 있는 항목을 추가한다. (Set이라서 순서 X, 중복 X)
print(week)


