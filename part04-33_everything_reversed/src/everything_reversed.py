# Write your solution here
def everything_reversed(my_list : list):
    new_list = []
    for i in reversed(my_list):
        new_list.append(i[::-1])   
    return new_list

if __name__ == "__main__":

    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)