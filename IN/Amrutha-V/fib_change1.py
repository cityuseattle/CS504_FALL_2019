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

while True:
    print ("What do you want to do?")
    choice = int(input("1. Find the number \n2. Exit\n"))
    if choice == 1:
        Fib_num = int(input("Enter a Fibonacci number: "))
        print(Fibonacci(Fib_num))
    elif choice == 2:
        break
    else:
        print ("Enter correct choice")