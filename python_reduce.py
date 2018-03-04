"""
The function reduce(func, seq) continually applies the function func() to the sequence seq.
It returns a single value.
"""
list1 = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, list1))
