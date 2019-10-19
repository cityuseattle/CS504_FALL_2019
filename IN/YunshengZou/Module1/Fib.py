# # Function for nth Fibonacci number 
  
# def Fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     # First Fibonacci number is 0 
#     elif n==1: 
#         return 0
#     # Second Fibonacci number is 1 
#     elif n==2: 
#         return 1
#     else: 
#         return Fibonacci(n-1)+Fibonacci(n-2) 
  
# # Driver Program 

# Fib_num = int(input("Enter a Fibonacci number: "))
# while Fib_num >= 1:
#     print(Fibonacci(Fib_num)) 
#     Fib_num = int(input("Enter a Fibonacci number: "))

# #This code is contributed by Saket Modi 
#========================================================
# fibonacci in using the loop
def loopFib(n):
    if n==1 or n==2:
        return 1
    a = b = 1
    c = 0
    for i in range(n - 2):
        c=a+b
        a=b
        b=c
    return c
#Driver Program
Fib_num = int(input("Enter a Fibonacci number:"))
while Fib_num >= 1:
    print(loopFib(Fib_num))
    Fib_num = int(input("Enter a Fibonacci number:"))
#Yunsheng-Zou