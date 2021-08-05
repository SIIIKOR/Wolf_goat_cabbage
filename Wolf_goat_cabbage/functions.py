""" Module with useful functions used in other parts of the program. """


from itertools import combinations
from collections import Counter


def dict_to_tuple(dictionary):
    """ Changes dictionary with int values to tuple. """
    output = []
    for key in dictionary:
        for i in range(dictionary[key]):
            output.append(key)
    return tuple(sorted(output))


def dict_to_list(dictionary):
    """
    We have to change our dict format to list in order to create combinations.
    We also don't include Human, because he later will be added.
    """
    output = []
    for key in dictionary:
        if key != "Human":
            for i in range(dictionary[key]):
                output.append(key)
    return output


def power_set(iterable, boat_size):
    """ We create all possible combinations(next states) with added human. """
    iterable = dict_to_list(iterable)
    output = []
    for i in range(boat_size):
        comb = combinations(iterable, i)
        for el in comb:
            new_el = ["Human"]
            for animal in el:
                new_el.append(animal)
            output.append(dict(Counter(new_el)))
    return output


def set_difference(a, b):
    """ Difference of set a and b. """
    output = {}
    for animal in a.contents:
        if animal not in b:
            output[animal] = a.contents[animal]
        else:
            val = a.contents[animal] - b[animal]
            if val:
                output[animal] = val
    return output


def tuple_difference(a, b):
    output = []
    for animal in a:
        if animal not in b:
            output.append(animal)
    return output
