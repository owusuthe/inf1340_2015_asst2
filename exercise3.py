#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    check_schema(table1, table2)
    result = []
    for row in table1[1:]:
        if row not in result:
            result.append(row)
    for row in table2[1:]:
        if row not in result:
            result.append(row)

    #Adds the row containing the schema to the result
    result = [table1[0]] + result

    return result

def intersection(table1, table2):
    """
    Checks if schema of tables are the same
    Returns a new table containing rows from both tables

    """
    check_schema(table1, table2)
    result = [item for item in table1[1:] if item in table2[1:]]

    #Adds the header to the result
    result = [table1[0]] + result

    return result


def difference(table1, table2):
    """
    Checks if schema of tables are the same
    Returns a new table containing rows from the first table but no in the second

    """
    check_schema(table1, table2)
    result = [item for item in table1[1:] if item not in table2[1:]]

    #Adds the row containing the schema to the result
    result = [table1[0]] + result

    return result


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

def check_schema(table1, table2):
    """
    A function that checks if schema of both tables are the same
    Compares if number of columns aren't the same
    Compares if name of columns aren't the same
    Raises a MismatchedAttributesException error if not the same
    """
    if not table1 or not table2:
        raise MismatchedAttributesException()

    headers1 = table1[0]
    headers2 = table2[0]

    if len(headers1) != len(headers2):
        raise MismatchedAttributesException()

    l = len(headers1)
    for i in range(l):
        if headers1[i] != headers2[i]:
            raise MismatchedAttributesException()
