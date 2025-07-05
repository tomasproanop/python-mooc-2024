# Write your solution here
def remove_smallest(numbers):
    smallest = numbers[0] # start at index 0

    for number in numbers: #for elem in list
        if number < smallest: #if elem is smaller than current index 
            smallest = number #make smallest equal to this number

    numbers.remove(smallest) #remove the smallest number
    #return numbers #return the modified list

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
