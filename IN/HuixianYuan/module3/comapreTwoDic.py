#compare two lists
firstlist=['cat', 'dog', 55]
secondlist=['dog', 55, 'cats']
print(firstlist==secondlist)

#order in dict does not matter
firstdist={'name':'Apiwat', 'species':'inhuman', 'age':'999'}
seconddist={'species':'inhuman', 'name':'Apiwat', 'age':'999'}
print(firstdist==seconddist)

mycat={'size':'small', 'color':'white', 'disposition':'loud'}
print('my cat has '+mycat['color']+ ' fur.')
print(mycat.get('color'))
print(mycat.keys())
print(mycat.values())
print(mycat.items())
