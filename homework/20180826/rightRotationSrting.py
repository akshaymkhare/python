#/usr/bin/python

"""

Program : Write a program to accept two strings from user and jumbled them (swapping of first two characters of both)

"""

def main():
	str01 = str(eval(input("Enter a string 01 : ")))
	str02 = str(eval(input("Enter a string 02 : ")))
	if str02 in (str01+str01):
		print(str02+" is right rotation of "+str01)
	else:
		print(str02+" is not right rotation of "+str01)

if __name__ == "__main__":
	main()