from functools import reduce

def sum_of_elements(numbers, exclude_negative = False):
    sum = 0
    if exclude_negative:
        positive_numbers = filter(lambda n: n > 0, numbers)
        sum = reduce(lambda x, y: x+y, positive_numbers)
    else:
        sum = reduce(lambda x, y: x+y, numbers)

    return sum

input_string = input("enter  a list of integers separated by spaces: ")
string_list = input_string.split()
numbers = list(map(int, string_list))

exclude_negative = False
exclude_negative_input = input("Exclude negative numbers? (yes/no): ").strip().lower()
exclude_negative = exclude_negative_input == 'yes'

print(sum_of_elements(numbers, exclude_negative))


