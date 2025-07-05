# Write your solution here
def sum_of_positives(list1):
    sum = 0

    for elem in list1:
        if elem > 0:
            sum = elem + sum
    return sum

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)