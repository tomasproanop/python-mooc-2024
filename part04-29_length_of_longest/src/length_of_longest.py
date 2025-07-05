# Write your solution here
def length_of_longest(list1):

    sizes = []

    for elem in list1:
        sizes.append(len(elem))

    greatest = max(sizes)
    return greatest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)