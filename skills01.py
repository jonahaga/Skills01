# Things you should be able to do.

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [5, 7, 2]
word_list = ['Python', 'Dog', 'One', 'Bike', 'Clipper', 'Projects', 'Obfuscation']
string_list = ['This', 'is', 'skills', '01' '.']

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd = []
    for i in some_list:
        if i % 2 != 0:
            odd.append(i)
    return odd

print all_odd(some_list)


# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even = []
    for i in some_list:
        if i % 2 == 0:
            even.append(i)
    return even

print all_even(some_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words = [] 
    for i in word_list:
        if len(i) >= 4:
            long_words.append(i)
    return long_words

print long_words(word_list) 

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return min(some_list)

print smallest(some_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return max(some_list)

print largest(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halvesies = []
    for i in some_list:
        div = float(i) / 2.0
        print div
    return halvesies

print halvesies(some_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list

print word_lengths(word_list)    

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print sum_numbers(numbers)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult = 1
    for i in numbers:
        mult = mult *i
    return mult 

print mult_numbers(numbers) 

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    single_string = ""
    for i in string_list:
        single_string = single_string + i + " "
    return single_string

print join_strings(string_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = sum_numbers(numbers)
    for i in numbers:
        average = float(total) / float(len(numbers))
    return average

print average(numbers)