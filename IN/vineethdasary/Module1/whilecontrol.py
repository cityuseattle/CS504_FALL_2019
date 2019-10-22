print('this program will sum the numbers from one to the number you enter.')
print("please enter a ending number.")
num = int(input())
total = 0

while num >=1 :
    total += num
    num -= 1

print('the total sum is: ' + str(total))