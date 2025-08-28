# local and global variable
rainfall = [45, 34, 23, 25, 53, 23]
location = 'Melbourne'


def print_rainfall(values):
    day = 1
    for value in values:
        print('Day', day, ':', value)
        day += 1


print_rainfall(rainfall)


def average_rainfall(values):
    import math
    return math.fsum(values) / len(values)


print(average_rainfall(rainfall))


def change_location(new_location):
    global location
    location = new_location
    print('new location is ', location)


print(location)
change_location('new york')
print(location)
