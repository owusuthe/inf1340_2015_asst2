#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    #For a given word in english, returns the word in pig latin

    :param : word
    :return: new_word + 'ay' or new_word + 'yay'
    :raises: except TypeError

    """
word = ""
#vowels = ('a', 'e', 'i', 'o', 'u')
#consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
vowels = ("aeiou")
consonants = ("bcdfghjklmnpqrstvwxyz")
"""
def pig_latinify(word):
    append_yay = "yay"
    append_ay = "ay"
    if word[0] in vowels:
        return word + append_yay
    elif word[0] in consonants:
        return word.lstrip("bcdfghjklmnpqrstvwxyz" ) + append_ay
    else:
        print "Enter a new word"

print pig_latinify("branch")


    #result = ""

    #return result
"""

word = ""
#vowels = ('a', 'e', 'i', 'o', 'u')
#consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
vowels = ("aeiou")
consonants = ("bcdfghjklmnpqrstvwxyz")

def pig_latinify(word):
    append_yay = "yay"
    append_ay = "ay"
    consonants_removed = word.lstrip(consonants)
    if word[0] in vowels:
        return word + append_yay
    elif word[0] in consonants:
        return consonants_removed + append_ay
    else:
        print "Enter a new word"
        
print pig_latinify("scratch")