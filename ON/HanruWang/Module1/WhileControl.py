print("This program will sum numbers from 1 to the num you enter.")
print("Please enter a number:")

num = int(input())
total = 0

while num >=1:
    total += num
    num -= 1

print("The sum is:" + str(total))