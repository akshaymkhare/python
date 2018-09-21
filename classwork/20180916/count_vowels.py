#/usr/bin/python

"""

Program : Write a program to accept a string from user and return count of vowels in it.

"""
def countVowels(input):
	vowels = "aeiouAEIOU"
	cnt = 0
	for x in input:
		if x in vowels:
			cnt += 1
	return cnt

def main():
	input_str = eval(input("Enter a string : "))
	print("Vowels count : ",countVowels(input_str))
	

if __name__ == "__main__":
	main()