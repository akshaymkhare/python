#/usr/bin/python

"""

Program : Write a program to display following pattern

1. Numbers Pyramid Pattern

      1
    2 1 2
  3 2 1 2 3
4 3 2 1 2 3 4

2. Water Mirror of ABCD pyramid pattern

D C B A B C D
  C B A B C
    B A B
      A

3. Toran by using * character

*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *

4. Mirror of Toran

* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *

5. Diamond using * character

    *
  * * *
* * * * *
  * * *
    *

"""



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
	pyramidNumbers(rows)
	(rows)

if __name__ == "__main__":
	main()