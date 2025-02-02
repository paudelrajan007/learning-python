# The Syntax

# newlist = [expression for item in iterable if condition == True]
# Example
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
item=[]
for i in range(1,4+1):
    fruits=str(input("Enter  fruits name :"))
    item.append(fruits)
newlist=[x for x in item if "a" in x]
print(newlist)