from itertools import *

# chain
# chain() function takes several iterators as arguments and returns a single iterator that produces
# the contents of all of them as though they came from a single sequence.
print(chain([1, 2, 3], ['a', 'b', 'c']))

# izip
# izip() returns an iterator that combines the elements of several iterators into tuples.
# It works like the built-in function zip(), except that it returns an iterator instead of a list.
print(izip([1, 2, 3], ['a', 'b', 'c']))
