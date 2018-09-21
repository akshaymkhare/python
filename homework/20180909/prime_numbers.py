#/usr/bin/python

"""

Program : Write a program to accept a range form user and display all prime numbers from given range.

"""
def isPrime(num):
	if (num<2):
		return False
	elif (num==2) or (num==3):
		return True
	elif (num%2 == 0):
		return False
	else:
		for x in range(3,int(num//2)+2,2):
			if (num%x == 0):
				return False
		else:
			return True

def prime_numbers(lb,ub):
	if (lb>0) and (ub>0):
		if (lb>ub):
			print("Lower bound number is smaller than upper bound number")
		else:
			primeNumLst = []
			for x in range(lb,ub):
				flag = isPrime(x)
				if (flag == True):
					primeNumLst.append(x)
			else:
				print("Prime numbers are :",primeNumLst)
	else:
		print("Please enter positive numbers of Lower bound and upper bound")
def main():
	lbNum,ubNum = eval(input("Enter a lower bound and upper bound numbers by using comma separated : "))
	prime_numbers(lbNum,ubNum)

if __name__ == "__main__":
	main()