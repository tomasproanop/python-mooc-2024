list1 = []

while True: 
    print(f"The list is now {list1}")
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "d":
        item = len(list1) + 1
        list1.append(item)
    elif command == "r":
        list1.remove(len(list1))
    elif command == "x":
        print("Bye!")
        break