print('This program will sum numbers from 1 to a number you enter.')
print('Please enter the number to end on: ')
num = int(input())
total = 0

while num >= 1:
    total += num
    num -= 1

print('The sum is: ' + str(total))