print('fatorial sum')
print('Enter ending number: ')
num = int(input())
total = 0

while num >= 1:
    total += num
    num -= 1

print('the sum is:  ' + str(total)) 