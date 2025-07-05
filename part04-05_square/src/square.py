# Copy here code of line function from previous exercise
def line(number, string):

    if string == "":
        print("*"*number)
    else:
        character = string[0]
        print(character*number)

def square(size, character):
    # You should call function line here with proper parameters
    counter = size
    line(size, character)
    while counter > 1:
        line(size, character)
        counter = counter - 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")