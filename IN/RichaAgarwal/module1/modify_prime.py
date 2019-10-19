# Python program to check if 
# given number is prime or not 
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
        
num = int(input("Enter a number: "))

# If given number is greater than 1 
if num > 1: 

  # Iterate from 2 to n / 2 
  for i in range(2, num//2): 
    # If num is divisible by any number between 
    # 2 and n / 2, it is not prime 
    if (num % i) == 0: 
      print(num, "is not a prime number")
      print_factors(num)
      break
    else: 
      print(num, "is a prime number")
      print_factors(num)
else:
  print(num, "is not a prime number")
  print_factors(num)
