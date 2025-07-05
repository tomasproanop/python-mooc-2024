# Copy here code of line function from previous exercise
def line(number, string):

    if string == "":
        print("*"*number)
    else:
        character = string[0]
        print(character*number)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    counter = size
    line(size, "#")
    while counter > 1:
        line(size, "#")
        counter = counter - 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
