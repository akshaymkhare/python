#/usr/bin/python

"""

Program : Write a program to accept two numbers from user and display their power

"""

def main():
	num01 = eval(input("Enter a number 01 : "))
	num02 = eval(input("Enter a number 02 : "))
	
	print("\n"+str(num01)+" Power "+str(num02)+" is : "+str(num01**num02))

if __name__ == "__main__":
	main()