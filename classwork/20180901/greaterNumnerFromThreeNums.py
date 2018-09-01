#/usr/bin/python

"""

Program : Write a program to accept 3 numbers form user and find maximum and minimum out of them

"""

def maxNumber(no1,no2,no3):
	if (no1 > no2) and (no1 > no3):
		print (str(no1)+" is a greater number")
	elif (no2 > no3):
		print (str(no2)+" is a greater number")
	else:
		print (str(no3)+" is a greater number")

def minNumber(no1,no2,no3):
	if (no1 < no2) and (no1 < no3):
		print (str(no1)+" is a smaller number")
	elif (no2 < no3):
		print (str(no2)+" is a smaller number")
	else:
		print (str(no3)+" is a smaller number")
		
def main():
	no1, no2, no3 = eval(input("Enter 3 numbers by comma separated : "))
	maxNumber(no1, no2, no3)
	minNumber(no1, no2, no3)
	
if __name__ == "__main__":
	main()