#/usr/bin/python

"""

Program : Write a program to accept a number form user and display fibonacci series up to number

"""

def fibonacci(no):
	if (no>0):
		tmpList = [0,1,1]
		current = 1
		pre = 1
		new = 0
		while(new<no):
			new = pre + current
			if (new<no):
				tmpList.append(new)
			pre = current
			current = new
		else:
			return tmpList

def main():
	num = eval(input("Enter a number : "))
	fiboList = fibonacci(num)
	print("Fibonacci series till number",num," : ",fiboList)

if __name__ == "__main__":
	main()