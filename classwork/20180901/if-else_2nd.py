#/usr/bin/python

"""

Program : 

"""

def main():
	donotsCount = eval(input("How many donuts you want ? : "))
	if (donotsCount <= 0):
		print("Incorrect Count")
	elif  (donotsCount <= 2):
		print("Too few Donuts")
	elif  (donotsCount <= 10):
		print("Donuts Count is "+str(donotsCount))
	elif  (donotsCount > 10):
		print("Too many Donuts")

if __name__ == "__main__":
	main()