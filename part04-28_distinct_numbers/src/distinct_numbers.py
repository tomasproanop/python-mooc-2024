# Write your solution here
def distinct_numbers(list1):
    unique = []
    elem = 0
    i = 0

    for elem in list1:
            if elem not in unique:
                unique.append(elem)

    return sorted(unique)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]