# Write your solution here
def all_the_longest(my_list : list):
    shortest = my_list[0]
    new_list = []
    for i in my_list:
        if len(i) >= len(shortest):
            shortest = i
        if shortest not in new_list:
            new_list.append(shortest)
        for item in new_list:
            if len(item) < len(shortest):
                new_list.remove(item)    
    return new_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']
