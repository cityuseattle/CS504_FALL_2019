income ={'Alice':9000,
         'Bob':10000,
         'Jeff':200000,
         'Apiwat':999998,
         'Stark':999999}

highest=max(income, key=income.get)
print('the richest man on the earth:', end=' ')
print(highest+' with $'+str(income[highest]))