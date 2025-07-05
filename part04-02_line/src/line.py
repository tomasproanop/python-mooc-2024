# Write your solution here
def line(number, string):

    if string == "":
        print("*"*number)
    else:
        character = string[0]
        print(character*number)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")