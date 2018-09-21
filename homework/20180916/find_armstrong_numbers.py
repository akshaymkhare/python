#/usr/bin/python

"""

Program : Write a program to accept range from user and print armstrong numbers from given range

"""

def isArmstrong(no):
	if (no>0):
		tempNum = 0
		while(no!=0):
			temp = no%10
			tempNum = tempNum + temp**3
			no = int(no//10)
		else:
			return tempNum

def findArmstrong(lb,ub):
	if (lb>0) and (ub>0):
		if (lb<ub):
			print("Armstrong list",end=" : ")
			for no in range(lb,ub+1):
				if (isArmstrong(no) == no):
					print(no,end=", ")
		else:
			print("Incorrect values")
	else:
		print("Incorrect values")

def main():
	lb,ub = eval(input("Enter lower bound and upper bound : "))
	results = findArmstrong(lb,ub)

if __name__ == "__main__":
	main()