#/usr/bin/python

"""

Program : Write a program to accept a string from user and display a string of first two and last two characters.

"""

def main():
	str01 = str(eval(input("Enter a string : ")))
	tempStr = str01[:-3:-1]
	print(str01[:2:1]+tempStr[::-1])

if __name__ == "__main__":
	main()