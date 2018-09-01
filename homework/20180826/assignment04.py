#/usr/bin/python

"""

Program : Write a program to accept a sentence from user and replace "not bad" with "good"

"""

def main():
	sentence = str(eval(input("Enter a sentence : ")))
	print(sentence.replace("not bad","good"))

if __name__ == "__main__":
	main()