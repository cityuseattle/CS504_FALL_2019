def Fibonacci(Fib_num):
    a,b = 0,1
    for i in range(Fib_num):
        a,b = b, a+b
    return a
    
Fib_num = int(input("Enter a Fibonacci number: "))
if Fib_num >= 1:
    print(Fibonacci(Fib_num)) 