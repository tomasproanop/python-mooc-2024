# Write your solution here
def most_common_character(string1: str):
    most_common = string1[0]
    for character in string1:
        if string1.count(character) > string1.count(most_common):
            most_common = character
    return most_common

# Write your solution here
def most_common_character(my_string: str):
    most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
 
    return most_common

if __name__ == "__main__":

    first_string = "aabbbbc"
    print(most_common_character(first_string))

    #second_string = "exemplaryelementary"
    #print(most_common_character(second_string))