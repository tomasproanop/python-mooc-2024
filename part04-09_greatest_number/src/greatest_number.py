# Write your solution here
def greatest_number(a, b, c):
    
    number_list = []
    number_list.append(a)
    number_list.append(b)
    number_list.append(c)

    return max(number_list)


    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)