# Write your solution here
list1 = []

while True:
    word = input("Word: ")

    if word in list1:
        print(f"You typed in {len(list1)} different words")
        break
    
    list1.append(word)