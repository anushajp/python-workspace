"""
filter out all the elements of a list, for which the function function returns True.
syntax :- filter(unction, iterable)
"""


def is_even(num):
    return True if num%2 == 0 else False

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filter out even numbers from list
print(filter(is_even, list1))  # output :- [2, 4, 6, 8]


# using lambda function with filter

# filter out the numbers greater than 5 from list1
print(filter(lambda x: x > 5, list1))  # output :- [6, 7, 8, 9]

# filter out odd numbers from the list
print(filter(lambda x: (x%2 != 0), list1))  # output :- [1, 3, 5, 7, 9]

