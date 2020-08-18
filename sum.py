# Up to and including "SQL Essential Training"

completed_hours = [2, 1, 6, 1, 1, 2, 2, 4, 2, 2, 1, 1, 1, 2, 4, 1, 1, 1, 2, 1, 2, 1, 2, 1, 5, 1, 1, 2, 2, 1, 2, 1, 1, 2,
                   2, 1, 2, 2, 2, 1, 1, 6, 2, 3, 2, 4, 1, 2, 2, 1, 1, 1, 1, 6, 3, 3, 2, 1, 2, 1, 1, 1, 2, 1, 3, 2, 4, 3]

completed_mins = [16, 13, 6, 38, 16, 11, 6, 45, 8, 31, 36, 39, 28, 17, 29, 45, 28, 58, 2, 25, 22, 30, 45, 57, 4, 45, 40,
                  58, 32, 3, 13, 55, 11, 25, 32, 49, 20, 4, 47, 17, 16, 22, 19, 13, 14, 25, 27, 39, 44, 59, 6, 5, 37,
                  41, 52, 15, 42, 10, 44, 8, 30, 55, 51, 27, 11, 59, 24, 47, 21, 25, 2, 44, 34, 14, 19, 44, 20, 14, 41,
                  41, 53, 23, 34, 17, 38, 54, 58, 3, 14]


def hours(list_of_hours):
    sum_hours = 0
    for num in list_of_hours:
        sum_hours += num

    return sum_hours


def minutes(list_of_mins):
    sum_mins = 0
    for num in list_of_mins:
        sum_mins += num

    return sum_mins


num_of_hours = int(hours(completed_hours))
num_of_mins = int(minutes(completed_mins))

mins_in_hours = num_of_mins / 60
total_hours = round((num_of_hours + mins_in_hours), 2)

print(f'Total hours: {total_hours}')
