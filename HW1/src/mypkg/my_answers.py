#!/usr/bin/python
#   Author : Wang Jinge
#   Date: 2/14/2019
"""
Python Core object Types
"""
from typing import Any


def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """

    #  Write square of 2018
    x = pow(2018, 2)
    print(x)

    # Assign a string "Stevens" to a variable y
    y = 'stevens'
    print(y)
    # Repeat variable y 5 times using *
    z = y
    new_list = [z] * 5
    print(new_list)
    # What is the length of z?
    length = len(z)
    print(length)
    # Concatenate variable y with string " is good"
    m = y + ' is good '
    print(m)
    # Replace "good" with "awesome" in variable m and assign it to a new variable n

    n = m.replace("good", "awesome")
    print(n)
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter 'space' into a list of substrings
    p = n.split(" ")
    print(p)
    # Get all the items except the first of the third substring
    r = n
    print(r[0:-7] + r[-6:])

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    A = [[1, 4, 5],
         [6, 10, 11],
         [12, 17, 38]]
    print(A)

    # Collect the items in the last column of matrix A using list comprehension
    c = [row[2] for row in A]
    print(c)

    # Collect only the even items of the diagonal of matrix A using list comprehension
    d = [A[i][i] for i in [0, 1, 2] if A[i][i] % 2 == 0]
    print(d)

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    o = [ord(y) for y in 'Stevens']
    print(o)
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f = {'fruit': 'apple',
         'quantity': 4,
         'color': 'green'}
    print(f)
    # Get the item in dictionary f that the key "fruit" maps to
    a = f['fruit']
    print(a)
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity'] = f['quantity'] + 1
    print(f)
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    amazing_grace = {'name': {'first_name': 'Grace', 'last_name': 'Hopper'}, 'jobs': ['scientist', 'engineer'],
                     'age': 85}
    print(amazing_grace)
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    amazing_grace['jobs'].append('programmer')
    print(amazing_grace)
    # Get the third job Grace has that you recently added
    p = amazing_grace['jobs'][2]
    print(p)
    # Get the sorted keys of amazing_grace in alphabetically ascending order
    k = list(amazing_grace.keys())
    k.sort()
    print(k)

    return a, f, p, k


numbers_and_strings()
lists()
dictionaries()
