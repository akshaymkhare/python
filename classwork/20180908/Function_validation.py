#/usr/bin/python

"""

Program : Function validation

"""

#Positional driven arguments
def add(a,b,c=0,d=0,e=0):
	return a+b+c+d+e

# Keyword driven arguments
def subt(a,b,c,d):
	return (a+b) - (c+d)

# Default arguments	in function
def slice(x,start,end,step=1):
	return x[start:end:step]

def add02(a,b,c=0,d=0,e=0):
	return a+b+c+d+e

def multi(a,b,c=1,d=1,e=1):
	return a*b*c*d*e
	
#Variable arguments function
def VariableArgs(*args):
	print("Type of arges : "+str(type(args)))
	for x in args:
		print(x)

def additionAnyNumbers(*args):
	temp=0
	for x in args:
		temp = temp+x
	return temp

def multiAnyNumbers(*args):
	temp=1
	for x in args:
		temp = temp*x
	return temp

#Variable Dictionary function
def VariableDictionayArgs(*args,**kwargs):
	print("Type of arges : "+str(type(args)))
	print("Type of kwarges : "+str(type(kwargs)))
	for x in args:
		print(x)
	print("\n")
	for y in kwargs:
		print(y,kwargs[y])
		
	
def main():
	'''
	print("Positional args Addition : "+str(add(1,2)))
	
	print("\nAddition 01 : "+str(add02(1,2)))
	print("Addition 02 : "+str(add02(1,2,3)))
	print("Addition 03 : "+str(add02(1,2,3,4)))
	print("Addition 04 : "+str(add02(1,2,3,4,5)))

	print("\nMultiplication 01 : "+str(multi(6,2)))
	print("Multiplication 02 : "+str(multi(6,2,3)))
	print("Multiplication 03 : "+str(multi(6,2,3,4)))
	print("Multiplication 04 : "+str(multi(6,2,3,4,5)))

	
	print("\nSubtract : "+str(subt(100,20,d=40,c=30)))
	print("Slicing : "+str(slice("Welcome",0,7)))
	
	print("\nVariableArgs 01 : "+str(VariableArgs(1)))
	print("\nVariableArgs 02 : "+str(VariableArgs(1,2,3,4)))
	print("\nVariableArgs 03 : "+str(VariableArgs(1,2,3,4,5,6,7,8,9,10,11,12,13,131,321,2313)))
	print("\nVariableArgs 04 : "+str(VariableArgs(10,"akshay",20,"khare")))
	print("\nVariableArgs 05 : "+str(VariableArgs("abc","dfc","asda","rfwr")))
	
	print("\nAddition of N no's : "+str(additionAnyNumbers(1,2,3,4,5,6,7,8,9,10,11,12,13,131,321,2313)))
	print("\nMultiplication of N no's : "+str(multiAnyNumbers(10,11,12,13,131)))
	'''
	
	print("\nVariable Dictionay Args 01 : "+str(VariableDictionayArgs(1,2,f_name="AKSHAY",l_name="KHARE",address="PUNE",age=31)))
	
	
if __name__ == "__main__":
	main()