# Write your solution here
def no_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    word = ""

    for index in string:
        if index in vowels:
            index = ""
        word += index
    return word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))