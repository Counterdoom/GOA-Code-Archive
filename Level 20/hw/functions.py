#Functions
def friend(x):
    return [name for name in x if len(name) == 4]

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

def double_char(s):
    result = ""
    for char in s:
        result += char * 2
    return result

def merge(a, b):
    result = str(a) + "," + str(b)
    return result

def even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
