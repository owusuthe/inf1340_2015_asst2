#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""


from exercise2 import find, multi_find


def test_find_basic():
    """
    Test find function.
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14
    assert find("ATCGATTCCGGATCGAAATCCGGAATCGATACG", "ATCG",  0, 32) == 0

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == 0,4,8,12
    assert multi_find("ATCGATCGATCGATCG", "ATCG", 0, 15) == 0,4,8,12

