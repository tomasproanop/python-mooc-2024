# init list
list1 = [1, 2, 3, 4, 5]

while True:

    # 5get input from user
    index = int(input("Index: "))

    if index == -1:
        break

    new_value = int(input("New value: "))

    list1[index] = new_value
    print(list1)