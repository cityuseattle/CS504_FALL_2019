# Function for nth Fibonacci number 
  
def Fibonacci(n):

    a = b = c = 1
    if n==1:
        return 1
    if n==2:
        return 2
        
    for i in range(3,n):

        c = a + b
        a = b
        b = c

        return c
  
  
# Driver Program 

Fib_num = int(input("Enter a Fibonacci number: "))
while Fib_num >= 1:
    print(Fibonacci(Fib_num)) 
    Fib_num = int(input("Enter a Fibonacci number: "))

#This code is contributed by Saket Modi 