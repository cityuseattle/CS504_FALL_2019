# Function for nth Fibonacci number 
  
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
  
# Driver Program 

loopContinued = input("Start? y/n: " )  #To descide if the loop continued or ended

while loopContinued == "y":
    Fib_num = int(input("Enter a Fibonacci number: "))
    if Fib_num >= 1:
        print(Fibonacci(Fib_num)) 
        loopContinued = input("Continue? y/n: " )

#This code is contributed by Saket Modi 