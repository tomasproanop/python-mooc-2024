# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word):

    return word == word[::-1]

    # string1 = word[len(word)//2:]
    # string2 = word[:len(word)//2]

    # if sorted(string1)==sorted(string2):
    #     print(word, "is a palindrome!")
    #     return True
    # else:
    #     print("that wasn't a palindrome")
    #     return False
    
    #print(string2, string1)

def main():
     while True:
        word = input("Please type in a palindrome: ")

        if palindromes(word):
            print(word, "is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
            continue

main()
