#/usr/bin/python

"""

Programs : 
1. Write a program to accept a number form user and print it in reverse order
2. Write a program to accept a number form user and to check if it is palindrome or not

"""

def reverseDigits(no):
	if (no>0):
		reverseNum = 0
		while(no!=0):
			reminder = no%10
			reverseNum = reverseNum*10 + reminder
			no = int(no//10)
		else:
			return reverseNum

def isPalindrome(no):
	pass

def main():
	num = eval(input("Enter a number : "))
	print("Reverse digits : ",reverseDigits(num))
	if (reverseDigits(num) == num):
		print ("\n",num,"is a palindrome")
	else:
		print ("\n",num,"is not a palindrome")
	

if __name__ == "__main__":
	main()