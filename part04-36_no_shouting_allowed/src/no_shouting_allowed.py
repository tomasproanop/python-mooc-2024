def no_shouting(strings):
    result = []
    for s in strings:
        if not s.isupper():
            result.append(s)
    return result

#def no_shouting(strings):
    # Create a new list containing only non-uppercase strings
 #   return [s for s in strings if not s.isupper()]

if __name__ == "__main__":
    print("XYZ".isupper())

    is_it_upper = "Abc".isupper()
    print(is_it_upper)