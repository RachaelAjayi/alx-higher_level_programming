#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = sorted(a_dictionary.items())
    for i in key_list:
        a, b = i
        print(f"{a}: {b}")
