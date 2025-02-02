# Python - List Comprehension 
items=[]
newitems=items

for _ in  range(1,4+1):
    fruits=str(input(f"Enter {_} fruits in the items: "))
    if "a" in fruits:
        items.append(fruits)
print(newitems)
