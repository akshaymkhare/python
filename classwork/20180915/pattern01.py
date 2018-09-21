#/usr/bin/python

"""

Program : Write a program to display following pattern

1. Pattern
*
**
***
****
*****

2. Mirror of pattern

3. Water image of pattern

4. pattern04
* * * *
  * * *
    * *
	  *

"""

def pattern01(rows):
	if (rows>0):
		print()
		for x in range(1,rows+1):
			for y in range(x):
				print("*\t", end="")
			print()
	else:
		print("Please enter a positive number of rows")

def pattern01OneLoop(rows):
	if (rows>0):
		print()
		temp = "*\t"
		for x in range(1,rows+1):
			print(temp*x)
	else:
		print("Please enter a positive number of rows")

def patternWaterImage(x):
	if (x>0):
		print()
		while (x>0):
			for y in range(x):
				print("*\t", end="")
			print()
			x-=1
	else:
		print("Please enter a positive number of rows")

def patternMirrorImage(rows):
	if (rows>0):
		print()
		for x in range(1,rows+1):
			for _ in range(rows-x):
				print("\t",end="")
			for _ in range(x):
				print("*\t", end="")
			print()
	else:
		print("Please enter a positive number of rows")
	
def patternMirrorWaterImage(rows):
	if (rows>0):
		print()
		for x in range(rows,0,-1):
			for _ in range(rows-x):
				print("\t",end="")
			for _ in range(x):
				print("*\t", end="")
			print()
	else:
		print("Please enter a positive number of rows")
'''
def charPattern01(rows):
	if (rows>0):
		print()
		tempChar = "A"
		count = 0
		for x in range(1,rows+1):
			count = 0
			for y in range(x):
				print(chr(ord(tempChar)+count),"\t", end="")
				count += 1
			print()
	else:
		print("Please enter a positive number of rows")

def charPattern02(rows):
	if (rows>0):
		print()
		tempChar = "A"
		count = rows
		for x in range(0,rows+1):
			count = rows
			for _ in range(rows-x):
				print("\t",end="")
				count -= 1
			for _ in range(x+1):
				print(chr(ord(tempChar)+count),"\t", end="")
				count -= 1
			for y in range(x):
				print(chr(ord(tempChar)+count),"\t", end="")
				count += 1
			print()
	else:
		print("Please enter a positive number of rows")
'''

def patternABCD01(rows):
	if (rows>0):
		for i in range(rows):
			k=65
			for j in range(i+1):
				print(chr(k+j)+"\t",end="")
			print()
	else:
		print("Please enter a positive number of rows")

def pyramidABCD(rows):
	if (rows>0):
		for i in range(1,rows+1):
			k = 64+i
			for _ in range(rows-i):
				print("\t",end="")
			for l in range(1,2*i):
				print(chr(k)+"\t",end="")
				if (l < i):
					k = k-1
				else:
					k = k+1
			print()
	else:
		print("Please enter a positive number of rows")

def pyramidNumbers(rows):
	pass

def pyramidABCDWaterImage(rows):
	pass
		
def main():
	rows = eval(input("Enter a rows count : "))
	'''
	print("============== Given Pattern ===================")
	pattern01(rows)
	print("\n============== Given Pattern using Single Loop ===================")
	pattern01OneLoop(rows)
	print("\n============== Pattern's Water Image ===================")
	patternWaterImage(rows)
	print("\n============== Mirror Image ===================")
	patternMirrorImage(rows)
	print("\n============== Mirror's Water Image ===================")
	patternMirrorWaterImage(rows)
	'''
	#charPattern01(rows)
	patternABCD01(rows)
	pyramidABCD(rows)

if __name__ == "__main__":
	main()