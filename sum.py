# Up to and including "pandas for Data Science"

completed_hours = [2, 2, 3, 6, 2, 3, 3, 1, 1, 0, 1, 1, 2, 1, 4, 2, 0, 2, 0, 1, 2, 1, 4, 2, 1, 6, 2, 1, 1, 0, 1, 2, 3,
                   1, 4, 1, 2, 1, 0, 0, 1, 1, 2, 1, 0, 2, 3, 1, 1, 2, 1, 2, 0, 2, 6, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 2,
                   1, 0, 0, 0, 1, 2, 0, 2, 0, 5, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


completed_mins = [3, 58, 54, 2, 19, 34, 44, 25, 21, 47, 24, 59, 27, 51, 55, 30, 44, 10, 57, 45, 30, 36, 45, 11, 38, 6,
                  16, 28, 39, 59, 24, 17, 0, 27, 14, 38, 17, 34, 53, 41, 41, 14, 20, 44, 14, 11, 8, 20, 25, 40, 45, 4,
                  58, 6, 46, 4, 49, 32, 13, 3, 58, 22, 25, 2, 28, 45, 15, 52, 41, 37, 5, 6, 59, 44, 47, 32, 39, 11, 55,
                  31, 8, 16, 13, 23, 25, 29, 17, 14, 13, 19, 22, 16]

print(f'\nTotal number of courses completed: {len(completed_mins)}')

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
