# Function for nth Fibonacci number 
  
def Fibonacci(n): 
    if n<=0: 
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
message = str(input("Play: (y/n)")).lower()
while message == "y":
    Fib_num = int(input("Enter a Fibonacci number: "))
    #Modified
    if Fib_num == 0:
        print(Fibonacci(Fib_num))
    else:
        count = 0
        while count < Fib_num:
            count+=1
            print(Fibonacci(count))
    message = str(input("Continue: (y/n)")).lower()
    while (message != "y" and message !=  "n"):
        message = str(input("Continue: (y/n)")).lower()
if message == "n":
    print("Bye")
