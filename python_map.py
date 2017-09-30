# syntax : map(aFunction, iterable)
"""
The map() function applies a given to function to each item of an iterable and returns a list of
the results.
"""


def add_10(num):
    """
    This function takes a number as argument and return the number by adding 10 to it
    """
    return num+10


def get_square(num):
    """
    This function takes a number as argument and return the square of the number
    """
    return num*num

# using map
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(map(add_10, sample_list))  # The result should be [11, 12, 13, 14, 15, 16, 17, 18, 19]
print(map(get_square, sample_list))  # The result should be [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map with lambda function

print(map(lambda x: x*x, sample_list))  # output should be [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(map(lambda x: x*2, sample_list))  # output should be [2, 4, 6, 8, 10, 12, 14, 16, 18]

# Passing Multiple Iterators to map() Using Lambda

list1 = [2, 3, 4, 5]
list2 = [5, 6, 7, 8]
print(map(lambda x, y: x+y, list1, list2)) # output should be [7, 9, 11, 13]

"""
If function is None, the identity function is assumed; if there are multiple arguments,
map() returns a list consisting of tuples containing the corresponding items
from all iterables (a kind of transpose operation). The iterable arguments may be a sequence or
any iterable object; the result is always a list:
"""

print(map(None, list1,list2))  # output :- [(2, 5), (3, 6), (4, 7), (5, 8)]


