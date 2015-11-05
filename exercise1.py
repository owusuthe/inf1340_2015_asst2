#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



"""
    #For a given English word, returns the word in Pig Latin form

    :param : word
    :return: word + 'ay' or word + 'yay'
    :raises: except TypeError

"""
vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")


def identify_vowel(word): #identify vowel in the english word

    for i in range(len(word)):
        if word[i] in vowels:
            return i

def pig_latinify(word):

    if word == type(int):
        raise TypeError('Invalid word')

    letters = word.split()
    count = 0
    result = ""

    for word in letters:
        vowel = identify_vowel(word)
        if vowel == -1: #first letter isn't a vowel
            result = word
        elif vowel == 0: #first letter is vowel
            result = word + "yay"
        else:#first letter is consonant
            result = word[vowel:] + word[:vowel] + "ay"

    return result




