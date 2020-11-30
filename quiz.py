# Problem:
#
# Saya is conducting an online Quiz competition daily where daily participation for
# contestants is optional. Saya want to send specific notifications to following group of participants
# Participants who participated everyday
# Participants who participated only once
# Participants who participated on the first day and never participated again.
#
# Help Saya to write functions in python to get the above information.
# Input:
# List of every day participant list
# Number of participants daily can be form 0 to 100000
# Number of days can be from 0 to 1000
# Output:
# List of participants who participated daily
# List of participants who participated only once
# List of participants who participated on the first day and never participated again.
# Sample input
# [
# [‘Sam’, ‘Emma’, ‘Joan’, ‘Krish’, ‘John’, ‘Desmond’, ‘Tom’, ‘Nicole’ ],
# [‘Brad’, ‘Walter’, ‘Sam’, ‘Krish’,’Desmond’, ‘Jennifer’],
# [‘Tom’, ‘Krish’, ‘Emma’, ‘Mia’, ‘Nicole’, ‘Sam’, ‘Desmond’],
# [‘Desmond’, ‘Sam’, ‘Krish’, ‘Mia’, ‘Harry’],
# [‘Ron’, ‘Ginny’, ‘Ted’, ‘Krish’, ‘Mia’, ‘Sam’, ‘Sachin’, ‘Desmond’, ‘Kapil’],
# [‘Krish’, ‘Brad’, ‘Walter’, ‘Jennifer’,’Desmond’, ‘Harry’, ‘Nicole’, ‘Sam’],
# ]
#
# Sample output
# [‘Desmond’, ‘Krish’, ‘Sam’]
# [‘Kapil’, ‘Ron’, ‘Ginny’, ‘Ted’, ‘Sachin’, ‘John’, ‘Joan’]
# [‘John’, ‘Joan’]


contestants_list = [
    ['Sam', 'Emma', 'Joan', 'Krish', 'John', 'Desmond', 'Tom', 'Nicole'],
    ['Brad', 'Walter', 'Sam', 'Krish', 'Desmond', 'Jennifer'],
    ['Tom', 'Krish', 'Emma', 'Mia', 'Nicole', 'Sam', 'Desmond'],
    ['Desmond', 'Sam', 'Krish', 'Mia', 'Harry'],
    ['Ron', 'Ginny', 'Ted', 'Krish', 'Mia', 'Sam', 'Sachin', 'Desmond', 'Kapil'],
    ['Krish', 'Brad', 'Walter', 'Jennifer', 'Desmond', 'Harry', 'Nicole', 'Sam']
]


def method1(contestants):
    """
    This function takes a list of daily participation and returns list of
    participants who participated everyday.
    """
    return list(set.intersection(*map(set, contestants)))


def method2(contestants):
    """
    The function return the list of participants who participated only once
    """
    total_data = [item for day_list in contestants for item in day_list]
    return list(filter(lambda x: total_data.count(x) == 1, total_data))


def method3(contestants):
    """
    The function return the list of participants who participated on the
    first day and never participated again.
    """
    # The value of day_check can be changed if the same check has to be done against other days
    day_check = 1
    day_data = contestants.pop(day_check-1)
    other_data = [item for day_list in contestants for item in day_list]
    return list(filter(lambda x: x not in other_data, day_data))


if __name__ == '__main__':
    result1 = method1(contestants_list)
    result2 = method2(contestants_list)
    result3 = method3(contestants_list)
    print('Participants who participated everyday --> %s' % result1)
    print('Participants who participated only once --> %s' % result2)
    print('Participants who participated on the first day and never participated again --> %s' % result3)
