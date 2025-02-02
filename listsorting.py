# Wap to short the list item .
fruits=[]
for _ in range(1,6+1):
    item=str(input(f"Enter {_} of fruits in the list : "))
    fruits.append(item)
fruits.sort()
remove=str(input("Enter what you want to remove from the list :"))
fruits.remove(remove)

print(fruits)
