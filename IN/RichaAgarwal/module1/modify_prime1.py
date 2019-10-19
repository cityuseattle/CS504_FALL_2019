# Python3 program to find the prime 
# numbers between a given interval 

if __name__ == '__main__': 
	
	# Declare the variables 
	a, b, i, j, flag = 0, 0, 0, 0, 0

	# Ask user to enter lower value of interval 
	print("Enter lower bound of the interval:", 
									end = "") 
	a = int(input()) # Take input 
	print(a) 
	
	# Ask user to enter upper value of interval 
	print("Enter upper bound of the interval:", 
									end = "") 
	b = int(input()) # Take input 
	print(b) 
	
	# Print display message 
	print("Prime numbers between", a, "and", 
						b, "are:", end = "") 

	# Traverse each number in the interval 
	# with the help of for loop 
	for i in range(a, b + 1): 

		# Skip 1 as1 is niether 
		# prime nor composite 
		if (i == 1): 
			continue

		# flag variable to tell 
		# if i is prime or not 
		flag = 1
		
		for j in range(2, i // 2 + 1): 
			if (i % j == 0): 
				flag = 0
				break
			
		# flag = 1 means i is prime 
		# and flag = 0 means i is not prime 
		if (flag == 1): 
			print(i, end = " ") 
