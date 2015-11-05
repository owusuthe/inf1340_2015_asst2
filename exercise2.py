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
    :return: match_start(int)
    :raises:

    """
search_area = input_string[start:end]
i = 0

match_start = -1

while 1 < len(search_area)-(len(substring)-1):
    letter = search_area(i)
    if letter == substring[0]:
        j = i + 1
        k = 1
while k < len(substring):



    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result

