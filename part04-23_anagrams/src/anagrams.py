# Write your solution here
def anagrams(word1, word2):
    w1 = sorted(word1)
    w2 = sorted(word2)

    if w1 == w2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False