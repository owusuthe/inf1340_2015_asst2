#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

WORKERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

STUDENTS = [["Number", "Surname"],
             [7274, "Robinson"],
             [7432, "O'Malley"],
             [9824, "Darkes"]]

TEACHERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

PRINCIPLES = [["Number", "Surname", "Years"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

ARTISTS = [["Number", "Surname", "Age"],
            [2899, "Richards", 46],
            [4566, "Jackson", 19],
            [5461, "Marks", 32]]





#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return t1.sort() == t2.sort()


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

    assert is_equal(result, union(MANAGERS, WORKERS))


def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))

    result = [["Number", "Surname", "Age"]]

    assert is_equal(result, intersection(GRADUATES, ARTISTS))


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))

    result = [['Number', 'Surname', 'Age'],
              [2899, 'Richards', 46], [4566, 'Jackson', 19],
              [5461, 'Marks', 32]]

    assert is_equal(result, intersection(ARTISTS, GRADUATES))



def test_number_columns_not_equal():
    """
    Test schema, if number of columns aren't the same.
    """

    try:
        union(STUDENTS, TEACHERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False


def test_column_names_not_equal():
    """
    Test schema, if names in column aren't the same.
    """

    try:
        difference(PRINCIPLES, TEACHERS)
    except MismatchedAttributesException:
        assert True
    else:
        assert False



