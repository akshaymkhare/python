"""
@gaol : Write a program to check whether the string is Symmetrical or Palindrome
@author : Akshay Khare
"""

def palindrome(input_str: str) -> bool:
    mid = (len(input_str)-1)//2
    flag = start = 0
    last = len(input_str)-1
    while (start < mid):
        if (input_str[start] == input_str[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break
    if (flag == 0):
        print("Regular : String is palindrome")
    else:
        print("Regular : String is not palindrome")

def symmetry(input_str: str):
    str_length = len(input_str)
    flag = 0
    if (str_length % 2):
        # For odd string length
        mid = str_length//2 + 1
    else:
        # For even string length
        mid = str_length//2
    str_start1 = 0
    str_start2 = mid
    while(str_start1 < mid and str_start2 < str_length):
        if (input_str[str_start1] == input_str[str_start2]):
            str_start1 += 1
            str_start2 += 1
        else:
            flag = 0
            break
    if (flag == 0):
        print("Regular : String is symmetrical")
    else:
        print("Regular : String is not symmetrical")

def palindrome_slicing(input_str: str):
    if (input_str == input_str[::-1]):
        print("Slicing : Entered string is palindrome")
    else:
        print("Slicing : Entered sting is not palindrome")

def symmetry_slicing(input_str: str):
    mid = int(len(input_str)/2)
    if (input_str[:mid] == input_str[mid:]):
        print("Slicing : Entered string is symmetrical")
    else:
        print("Slicing : Entered string is not symmetrical")

def main():
    input_string = input("Enter a string to check whether string is Symmetrical or Palindrome: ")
    palindrome(input_string)
    symmetry(input_string)
    palindrome_slicing(input_string)
    symmetry_slicing(input_string)

if __name__ == "__main__":
    main()