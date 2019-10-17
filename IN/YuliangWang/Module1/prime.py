# Python program to check if the input number is prime or not
# take input from the user
# num = int(input("Enter a number: "))
num=int(input("please enter a number: "))
#create an array to save factors
fac = []
# prime numbers are greater than 1
if num > 1:
    
# check for all factors
   for i in range(1,num+1):
           if(num % i)==0:
            print(i,"times",num//i,"is",num)
            fac.append(i)
            continue
           else:
                pass

# if input number is less than
# or equal to 1, it is not prime
if num <=1:
   print(str(num) + " is not a prime number")

#check if the input number is prime or not
if fac==[]:
    print(str(num) + ' is a prime number')
else:
    print(str(num) + ' is not a prime number')
    print(fac)   