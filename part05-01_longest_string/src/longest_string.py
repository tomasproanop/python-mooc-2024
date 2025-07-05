# Write your solution here
def longest(strings: list):
    elem = ""
    for item in strings:
        if len(item) > len(elem):
            elem = item
    return elem

# alternative
# def longest(strings):
#     longest = ""
#     for string in strings:
#             if string > longest:
#                 longest = string
#     return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))

