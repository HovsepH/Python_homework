def classify_numbers(number_list):
    odd_numbers = []
    even_numbers = []
    
    for num in number_list:
        if num % 2 != 0:
            odd_numbers.append(num)
        else:
            even_numbers.append(num)

    return odd_numbers, even_numbers
    



input_str = input("enter a list of numbers separated by spaces:\n")
string_list =  filter(lambda s: s != ' ', input_str)
number_list = list(map(int, string_list))

result = classify_numbers(number_list)

print(f"Even numbers: {result[1]}")
print(f"Odd numbers: {result[0]}")