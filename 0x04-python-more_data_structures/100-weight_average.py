#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_scores = 0
    sum_weights = 0

    for score, weight in my_list:
        sum_scores += score * weight
        sum_weights += weight
    if sum_weights == 0:
        return 0
    average = sum_scores / sum_weights
    return average
