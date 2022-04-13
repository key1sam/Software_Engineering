'''Exercise 13) Write a Python program to concatenate the existing
dictionaries to create a new one. '''
Dic1 = {1:10, 2:20}
Dic2 = {3:30, 4:40}
Dic3 = {5:50, 6:60}

Dic1.update(Dic2)
Dic1.update(Dic3)
print(Dic1)
