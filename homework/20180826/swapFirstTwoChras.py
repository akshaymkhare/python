#/usr/bin/python

"""

Program : Write a program to accept two strings from user and jumbled them (swapping of first two characters of both)

"""

def main():
	str01 = str(eval(input("Enter a string 01 : ")))
	str02 = str(eval(input("Enter a string 02 : ")))
	print("\nModified Strings \n\nString 01 : "+str02[0:2]+str01[2::]+"\nString 02 : "+str01[0:2]+str02[2::])

if __name__ == "__main__":
	main()