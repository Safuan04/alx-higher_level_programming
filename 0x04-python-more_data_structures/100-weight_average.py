#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    final_weight = 0
    weight_sum = 0

    for i in my_list:
        final_weight += i[0] * i[1]
        weight_sum += i[1]

    return final_weight / weight_sum
