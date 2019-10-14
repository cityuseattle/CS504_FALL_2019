# Python program to check if the input number is prime or not

# take input from the user

num = int(input("Enter a number: "))
is_prime = True

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(i,"times",num//i,"is",num)
           is_prime = False
       
if is_prime == True:
   print(num,"is a prime number")
if is_prime == False:
   print(num,"is not a prime number")