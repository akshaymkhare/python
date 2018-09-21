#/usr/bin/python

"""

Program : write a program to accept a number from user and check if it is multiple of 16 or not without using arithmetic operators  (Try bitwise operators)

"""

def main():
	num01 = eval(input("Enter a number : "))
	if ((num01 & 15) == 0):
		print ("Number  {} is multiple of 16".format(num01))
	else:
		print ("Number {} is not multiple of 16".format(num01))

if __name__ == "__main__":
	main()