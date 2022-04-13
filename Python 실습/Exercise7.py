_list = ['Red', 'Green', 'White', 'Black', 'Yellow' ,'Pink', 'Blue']
removeKey = []
removeKey.append(_list[0])
removeKey.append(_list[4])
removeKey.append(_list[5])

for k in removeKey:
    _list.remove(k)

print(_list)