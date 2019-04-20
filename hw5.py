#!/usr/bin/python

"""
Python Functions and Recursions
"""


"""
QUESTION 1: 
========================================================================================================

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(n):
    res = []
    helper(n, n, '', res)
    return res


def helper(l, r, item, res):
    if l == 0 and r == 0:
        res.append(item)
    if l > 0:
        helper(l - 1, r, item + '(', res)
    if r > l:
        helper(l, r - 1, item + ')', res)
"""
QUESTION 2: 
========================================================================================================

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
=========================================
Input: "race a car"
Output: false

Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""


def isPalindrome(s):
    if len(s) == 0:
        return True
    i = 0
    j = len(s)-1
    while i < j:
        while not s[i].isalnum():
            i += 1
        while not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


