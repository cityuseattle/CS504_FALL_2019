#compare two list, two dicts
firstlist = ['cats','dogs',55]
secondlist = ['dogs',55,'cats']
print(firstlist == secondlist)

firstDict= {'name':'Apiwat', 'species':'inhuman', 'age':'999'}
secondDict={'species':'inhuman', 'age':'999','name':'Apiwat'}
print(firstDict==secondDict)

myCat = {'size':'small', 'color':'white','disposition':'loud'}
print('My cat has ' + myCat['color']+ 'fur.')