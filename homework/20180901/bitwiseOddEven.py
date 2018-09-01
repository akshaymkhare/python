#/usr/bin/python

"""

Program : write a program to accept a number from user and print if it is even or odd  without using arithmetic operators  (Try bitwise operators)

"""

def main():
	num01 = eval(input("Enter a number : "))
	if ((num01 & 1) == 1):
		print ("Number is Odd")
	else:
		print ("Number is Even")

if __name__ == "__main__":
	main()