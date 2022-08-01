from cgi import test
from datetime import date, datetime, timedelta

date_dict = {date(2022, 11, 17):  0.03, date(2023, 11, 17):  0.04, date(
    2024, 11, 17):  0.05, date(2025, 11, 17):  0.06, date(2026, 11, 17):  0.07}

date_dict_list = list(date_dict.keys())
yield_dict_list = list(date_dict.values())


test_date = date(2022, 12, 17)

#Add use case for lower than smallest benchmark and greater than largest benchmark

diff_list = []

for i in date_dict_list:
    diff_list.append((i-test_date))

print(diff_list)

closest_index = diff_list.index(min(diff_list))
closest_date = min(diff_list)
closest_two = ()

print(closest_index)

if closest_date < timedelta(days=0):
    closest_two = (closest_index, closest_index + 1)
else:
    closest_two = (closest_index, closest_index - 1)

lower_difference = test_date - date_dict_list[closest_two[0]]
upper_difference = -1 * (test_date - date_dict_list[closest_two[1]])

print(lower_difference, upper_difference)

lower_weight = 1 - float(lower_difference.days/365)
upper_weight = 1 - float(upper_difference.days/365)

print(yield_dict_list[closest_two[0]] * lower_weight +
      yield_dict_list[closest_two[1]] * upper_weight)
