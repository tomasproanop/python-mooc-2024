# Write your solution here
while True:
    string = input("Editor: ")

    if string.lower() == "notepad" or string.lower() == "word":
        print("awful")
    elif string.lower() == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
