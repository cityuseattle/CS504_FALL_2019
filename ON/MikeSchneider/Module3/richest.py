income = {'Alice': 9000, 
    'Bob': 100000, 'Jeff': 200000, 
    'Apiwat': 99999, 'Stark': 999999}

highest = max(income, key=income.get)
print("The richest man on earth: ", end=' ')
print(highest + ' with $' + str(income[highest]))
