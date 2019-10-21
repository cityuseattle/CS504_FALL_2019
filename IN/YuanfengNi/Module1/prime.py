# Python program to check if the input number is prime or not
# if it is not, show all factors

# take input from the user
num = int(input("Enter a number: "))
a = 0
   # show all the factors, otherwise show num is prime
for i in range(2,num):
   if (num % i) == 0:
      print(i,"times",num//i,"is",num)
      a = a + 1
if a > 0:
   print(num,"is not a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is a prime number")


