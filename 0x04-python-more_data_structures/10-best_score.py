#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max_score = 0
    max_student = None
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_student = key
    return max_student
