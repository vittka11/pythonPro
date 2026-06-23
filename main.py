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

def get_square(number):
    square = number ** 2
    return square
user_number = float(input("Enter a number:"))
result = get_square(user_number)
print("Square of the number:", result)

def get_sum(first_number, second_number):
    total = first_number + second_number
    return total
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = get_sum(number1, number2)
print("Sum:", result)

def divide_numbers(first_number, second_number):
    quotient = first_number // second_number
    remainder = first_number % second_number
    return quotient, remainder
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))
quotient, remainder = divide_numbers(number1, number2)
print("Quotient:", quotient)
print("Remainder:", remainder)