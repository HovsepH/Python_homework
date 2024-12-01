import functools
import time

with open(r"C:\repos\homework_py\lec_12\random_numbers.txt", 'r') as file:
    for line in file:
        string_list = line.split()
        numbers = list(map(int, string_list))
        print(numbers)

result = []
with open(r"C:\repos\homework_py\lec_12\random_numbers.txt", 'r') as file:
    for line in file:
        string_list = line.split()
        result.append(list(filter(lambda n: int(n) > 40, string_list)))
print(result)


with open(r"C:\repos\homework_py\lec_12\random_numbers.txt", 'w') as file:
    for row in result:
        line = ' '.join(map(str, row))
        file.write(line+"\n")

def measure_exec_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time-start_time}")
        return result
    return wrapper


def read_file_as_generator(path):
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()


@measure_exec_time
def print_file():
    for line in read_file_as_generator(r"C:\repos\homework_py\lec_12\random_numbers.txt"):
        print(line)

print_file()