#/usr/bin/python

"""

Program : Write a program to accept a number form user and to check if it is armstrong

"""

def armstrongNum(no):
	if (no>0):
		tempNum = 0
		while(no!=0):
			temp = no%10
			tempNum = tempNum + temp**3
			no = int(no//10)
		else:
			return tempNum

def main():
	num = eval(input("Enter a number : "))
	if (armstrongNum(num) == num):
		print ("\n",num,"is a armstrong number")
	else:
		print ("\n",num,"is not a armstrong number")
	

if __name__ == "__main__":
	main()