#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
    """
    Basic test cases from assignment hand out
    """

    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"


def test_unexpected_word():
    try:
        pig_latinify(3)
    except ValueError:
        assert True
    else:
        assert False


def test_multiple_word():
    try:
        pig_latinify("apple happy")
    except ValueError:
        assert True
    else:
        assert False


def test_capitalize_word():
    try:
        pig_latinify("Happy")
    except ValueError:
        assert True
    else:
        assert False


