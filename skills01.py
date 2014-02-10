
# Things you should be able to do.

# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some_list = ['A', 'Dog', 'One', 'Bike', 'Clipper', 'Projects', 'Obfuscation', 3, 5, 6, 8, 16]
numbers = [5, 7, 2]
word_list = ['Python', 'Dog', 'One', 'Bike', 'Clipper', 'Projects', 'Obfuscation']
string_list = ['This', 'is', 'skills', '01' '.']

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    odd = []
    for i in some_list:
        if type(i) is not str:
            if i % 2 != 0:
                odd.append(i)
    return odd

print "All Odd:",all_odd(some_list)

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even = []
    for i in some_list:
        if type(i) is not str:
            if i % 2 == 0:
                even.append(i)
    return even

print "All Even:", all_even(some_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    long_words = [] 
    for i in word_list:
        if len(i) >= 4:
            long_words.append(i)
    return long_words

print "Long Words:", long_words(word_list) 

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = None
    for i in range(len(some_list)):
        if type(some_list[i]) is not str:
            if smallest == None or some_list[i] < smallest:
                smallest = some_list[i]
    return smallest

print "Smallest:", smallest(some_list)

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = None
    for i in range(len(some_list)):
        if type(some_list[i]) is not str:
            if largest == None or some_list[i] > largest:
                largest = some_list[i]
    return largest

print "Largest:", largest(some_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    halvesies = []
    for i in some_list:
        if type(i) is not str:
            div = float(i) / 2.0
            halvesies.append(div)
    return halvesies

print "Halvsies:", halvesies(some_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list

print "World Lengths:", word_lengths(word_list)    

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

print "Sum Numbers:", sum_numbers(numbers)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult = 1
    for i in numbers:
        mult = mult *i
    return mult 

print "Mult Numbers:", mult_numbers(numbers) 

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    single_string = ""
    for i in string_list:
        single_string = single_string + i + " "
    return single_string

print "Join Strings:", join_strings(string_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = sum_numbers(numbers)
    for i in numbers:
        average = float(total) / float(len(numbers))
    return average

print "Average:", average(numbers)