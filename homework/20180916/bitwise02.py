#/usr/bin/python

"""

Program : Write a program to accept a number from user and number of bits to TURN ON/OFF/TOGGLE from right most sides.

"""

def turnOn(num,noBits):
	no = (2**noBits) - 1
	return (num | no)

#Not sure this function is correctly working
def	turnOff(num,noBits):
	no = (2**noBits) - 1
	return (num & no)

#Not sure this function is correctly working
def	turnToggle(num,noBits):
	no = (2**noBits) - 1
	return (num ^ no)

def main():
	num = eval(input("Enter a number to perform a bits operation TURN ON | OFF | TOGGLE : "))
	noBits = eval(input("Enter how many bits need to perform operation from right most side : "))
	print("{} turn ON bits by {} : {}".format(num,noBits,turnOn(num,noBits)))
	print("{} turn OFF bits by {} : {}".format(num,noBits,turnOff(num,noBits)))
	print("{} TOGGLE bits by {} : {}".format(num,noBits,turnToggle(num,noBits)))
	
if __name__ == "__main__":
	main()