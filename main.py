#def get_string_length(text):
    #length = len(text)
    #return length
#user_text = input("Enter a string: ")
#result = get_string_length(user_text)
#print("String length:", result)

#def join_strings(first_string, second_string):
    #combined_string = first_string + second_string
    #return combined_string


#text1 = input("Enter the first string: ")
#text2 = input("Enter the second string: ")

#result = join_strings(text1, text2)

#print("Combined string:", result)

#def get_square(number):
    #square = number ** 2
    #return square
#user_number = float(input("Enter a number:"))
#result = get_square(user_number)
#print("Square of the number:", result)

#def get_sum(first_number, second_number):
#    total = first_number + second_number
    #return total
#number1 = float(input("Enter the first number: "))
#number2 = float(input("Enter the second number: "))
#result = get_sum(number1, number2)
#print("Sum:", result)

#def divide_numbers(first_number, second_number):
    #quotient = first_number // second_number
    #remainder = first_number % second_number
    #return quotient, remainder
#number1 = int(input("Enter the first integer: "))
#number2 = int(input("Enter the second integer: "))
#quotient, remainder = divide_numbers(number1, number2)
#print("Quotient:", quotient)
#print("Remainder:", remainder)

def calculate_average(numbers):
    average = sum(numbers) / len(numbers)
    return average
numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("Average:", result)

def find_common_elements(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements
first_list = [1, 2, 3, 4, 5]
second_list = [3, 4, 5, 6, 7]
result = find_common_elements(first_list, second_list)
print("Common elements:", result)

def print_keys(dictionary):
    for key in dictionary:
        print(key)
student = {
    "name": "John",
    "age": 20,
    "city": "London"
}
print_keys(student)

def merge_dictionaries(dict1, dict2):
    merged_dictionary = dict1.copy()
    merged_dictionary.update(dict2)
    return merged_dictionary
first_dict = {
    "name": "John",
    "age": 20
}
second_dict = {
    "city": "London",
    "country": "UK"
}
result = merge_dictionaries(first_dict, second_dict)
print(result)

def union_sets(set1, set2):
    result = set1.union(set2)
    return result
first_set = {1, 2, 3}
second_set = {3, 4, 5}
result = union_sets(first_set, second_set)
print(result)

def is_subset(set1, set2):
    return set1.issubset(set2)
small_set = {1, 2}
big_set = {1, 2, 3, 4, 5}
result = is_subset(small_set, big_set)
print(result)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(result)

def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = get_even_numbers(numbers)
print(result)
check_even_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
print(check_even_odd(10))
print(check_even_odd(7))