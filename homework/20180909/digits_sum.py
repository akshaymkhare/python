#/usr/bin/python

"""

Programs : 

1. Write a program to accept a number form user and display sum of its digits
2. Write a program to accept a number form user and display even digits sum and odd digits sum
3. Write a program to accept a number form user and display difference of even and odd digits sum


"""

def digitsSum(no):
	if(no>0):
		tempSum = 0
		while(no!=0):
			tempSum = tempSum + no%10
			no = int(no/10)
		else:
			return tempSum

def evenDigitsSum(no):
	if(no>0):
		tempevenSum = 0
		while(no!=0):
			temp = no%10
			if (temp%2 == 0):
				tempevenSum = tempevenSum + temp
			no = int(no/10)
		else:
			return tempevenSum

def	oddDigitsSum(no):
	if(no>0):
		tempOddSum = 0
		while(no!=0):
			temp = no%10
			if (temp%2 != 0):
				tempOddSum = tempOddSum + temp	
			no = int(no/10)
		else:
			return tempOddSum
			
def main():
	num = eval(input("Enter a number : "))
	print("Digits Sum : ",digitsSum(num))
	print("Even Digits Sum : ",evenDigitsSum(num))
	print("Odd Digits Sum : ",oddDigitsSum(num))

if __name__ == "__main__":
	main()