# Write your solution here
items = int(input("How many items: "))

list = []
counter = 1

while items >= 1:
    item = int(input(f"Item {counter}: 5"))
    list.append(item)
    items -= 1
    counter += 1

print(list)