#/usr/bin/python

"""

Program : Write a program to check the given number is special number

"""

def factorialNum(no):
	cnt = 1
	while(no>0):
		cnt = cnt * no
		no = no - 1
	else:
		return cnt

def isSpecialNumber(num):
	if (num > 0):
		sum = 0
		while(num!=0):
			temp = num%10
			sum = sum + factorialNum(temp)
			num = int(num//10)
		else:
			return sum
	else:
		print("Incorrect number")
		
def main():
	num = eval(input("Enter a numbmer to check it for special number : "))
	if (isSpecialNumber(num) == num):
		print("{} is a special number".format(num))
	else:
		print("{} is not a special number".format(num))

if __name__ == "__main__":
	main()