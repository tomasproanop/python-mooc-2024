# Copy here code of line function from previous exercise and use it in your solution
def line(number, string):

    if string == "":
        print("*"*number)
    else:
        character = string[0]
        print(character*number)

def shape(number1, char1, number2, char2):
        
    index1 = 1
    while index1 <= number1:
        line(index1, char1)
        index1 += 1
    
    index2 = 1
    while index2 <= number2:
        line(number1, char2)
        index2 += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")