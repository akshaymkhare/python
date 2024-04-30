"""
Problem statement : Write a program in python to interchange a first and last number from a list
Auther : Akshay Khare
"""


# Using Pop-Append
# ----------------
def interchangeFirstLastElement_usingPopAppend(input_lst):
    first = input_lst[0]
    last = input_lst[-1]
    input_lst.pop(-1)
    input_lst.pop(0)
    input_lst.insert(0, last)
    input_lst.append(first)
    return input_lst


# Using slicing
# --------------
def interchangeFirstLastElement_usingSlicing(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst


# Swap elements using python simple way
# --------------------------------------
def interchangeFirstLastElement_usingSimpleWay(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


# Swap function
# -------------
def interchangeFirstLastElement_usingSwap(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList


def main():
    input_list = []
    input_list_count = int(input("Please enter number of list elements count : "))
    for i in range(input_list_count):
        input_element = input("Enter a element : ")
        input_list.append(input_element)
    print(f"Before interchange : {input_list}")
    print(f"After interchange using pop-append: {interchangeFirstLastElement_usingPopAppend(input_list)}")
    print(f"\nBefore interchange : {input_list}")
    print(f"After interchange using slicing : {interchangeFirstLastElement_usingSlicing(input_list)}")
    print(f"\nBefore interchange : {input_list}")
    print(f"After interchange using python simple way : {interchangeFirstLastElement_usingSimpleWay(input_list)}")
    print(f"\nBefore interchange : {input_list}")
    print(f"After interchange using swap function : {interchangeFirstLastElement_usingSwap(input_list)}")


if __name__ == "__main__":
    main()
