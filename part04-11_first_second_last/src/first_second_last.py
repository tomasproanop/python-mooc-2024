# Write your solution here

def first_word(sentence):
    array1 = sentence.split(" ")
    word = array1[0]
    return word

def second_word(sentence):
    array1 = sentence.split(" ")
    word = array1[1]
    return word

def last_word(sentence):
    array1 = sentence.split(" ")
    index = len(array1) - 1
    word = array1[index]
    return word


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))