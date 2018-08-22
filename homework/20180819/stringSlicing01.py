#/usr/bin/python

"""

Program : Write a program to accept a string from user and accept the start-index, end-index and step value from user. Display a string accordingly"

"""

def main():
	input_string = input("Enter a string : ")
	start_index = eval(input("Enter start index : "))
	end_index = eval(input("Enter end index : "))
	step_value = eval(input("Enter step value : "))
	
	if (len(input_string) > 0):
		print("\nOriginal String :: "+str(input_string)+" \nScliced string :: "+str(input_string[start_index:end_index:step_value]))
	else:
		print("\nInvalid String ...")

if __name__ == "__main__":
	main()