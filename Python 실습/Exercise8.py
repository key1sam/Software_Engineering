list1 = ['Red', 'Green', 'White', 'Black', 'Yellow', 'Pink', 'Blue']
list2 = ['Red', 'Green', 'Black', 'White', 'Yellow', 'Indigo','Blue']
answer = []

for i in range(7) :
    if list1[i] != list2[i] :
        answer.append((i, list1[i], list2[i]))
print(answer)