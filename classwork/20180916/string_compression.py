#/usr/bin/python

"""

Program : Write a program to accept a string from user and perform compression on it.

"""
def compressedString(input):
	ouputStr = ""
	n = 0
	while(n<len(input)):
		count = 1
		tmpChr = input[n]
		while((n+1<len(input)) and (tmpChr == input[n+1])):
			n += 1
			count+=1
		ouputStr = ouputStr+tmpChr+str(count)
		n += 1
	return ouputStr

def main():
	input_str = eval(input("Enter a string : "))
	print("Compressed string : ",compressedString(input_str))
	

if __name__ == "__main__":
	main()