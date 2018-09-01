#/usr/bin/python

"""

Program : Write a program to accept a string from user and display it reserver

"""

def main():
	string01 = eval(input("Enter a string : "))
	
	print("\n Original String : "+string01+"\n Reverse String : "+str(string01[::-1]))

if __name__ == "__main__":
	main()