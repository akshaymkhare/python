#/usr/bin/python

"""

Program : Write a program to accept a lower bound and upper bound form user and display tables

"""

def tables(n):
	print (n,"'s Table :\n")
	for y in range (1,11):
		print(n,"*",y,"=",n*y)
	print ("===============")
	
def main():
	lb,ub = eval(input("Enter a lower and upper bound to display the tables : "))
	if (lb<ub):
		for x in range(lb,ub+1):
			tables(x)
	else:
		print("Enter lower bound value less than upper bound")

if __name__ == "__main__":
	main()