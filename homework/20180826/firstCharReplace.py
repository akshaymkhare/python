#/usr/bin/python

"""

Program : Write a program to accept a string from user and replace the occurrence of first Character in remaining string with '*'

"""

def main():
	str01 = str(eval(input("Enter a string : ")))
	tempStr = str01.replace(str01[0],'*')
	print(str01[0]+tempStr[1::])

if __name__ == "__main__":
	main()