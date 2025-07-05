# Write your solution here
list1 = []
while True:
    number = int(input("New item: "))

    if number == 0:
        print("Bye!")
        break

    list1.append(number)

    print(f"The list now: {list1}")
    print(f"The list in order: {sorted(list1)}")