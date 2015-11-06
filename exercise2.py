#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param : input_string (string)
    :return:
    :raises:

    """
    #search_area = input_string[start:end]

    i = start


    while i < len(input_string):
        if input_string[i:i+len(substring)] == substring:
            return i
        i += 1


    return -1


def multi_find(input_string, substring, start, end):
    """
    call find function from above
    input input_string, substring, start, and end as given in multi_find
    store returned values in the result string
    if find function does not find substring, then return the empty string
    otherwise the indices of substring occurrences are returned in the result string
    Describe your function

    :param :
    :return:
    :raises:

    """

    result = ""

    i = start

    while i < len(input_string):

        i = find(input_string, substring, i, end)
        if i >= 0:
            result += str(i) + ","
            i += 1
        else:
            return result[0: len(result)-1]
        #this last function is because the string returns a comma for the last index value as well

    return result
