print('This program will sum the numbers from1 toa  number you enter.')
print('Please enter a ending number:')
num = int(input())
total = 0

while num >= 1:
    total += num
    num -= 1

    print('The sum is: ' + str(total))