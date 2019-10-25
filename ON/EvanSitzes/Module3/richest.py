income = {
    'Alice': 4000,
    'Bob': 5000,
    'John': 6700,
    'Evan': 9989,
    'Stark': 9999
}

highest = max(income, key=income.get)

print('Richest person on the earth: ')
print(highest + ' with $' + str(income[highest]))
