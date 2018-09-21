#/usr/bin/python

"""

Program : Write a program to accept a lower bound and upper bound from user and display multiple of 5 in it

"""

def forLoop(LB,UB):
	print("\n+++++++ For Loop ++++++++")
	for x in range(LB,UB+1):
		if ((x%5) == 0):
			print("{} is a multiple of 5".format(x))

def whileLoop(LB,UB):
	print("\n+++++++ While Loop ++++++++")
	while(LB<=UB):
		if ((LB%5) == 0):
			print("{} is a multiple of 5".format(LB))
		LB+=1
		
def main():
	LB = eval(input("Enter a lower bound number : "))
	UB = eval(input("Enter a upper bound number : "))

	if (LB > UB):
		print ("Please enter lower bound number less than upper bound")
	else:
		forLoop(LB,UB)
		whileLoop(LB,UB)

	
if __name__ == "__main__":
	main()