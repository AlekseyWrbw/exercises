'''
Given an integer x, return true if x is a
palindrome
, and false otherwise.
'''

class Solution(object):
    def isPalindrome(self, x):
        array = list(str(x))
        reverse_array = []
        for k in range(0, len(array)):
            reverse_array.append(array[len(array) - 1 - k])
        reverse_string = ''.join(reverse_array)
        if reverse_string == str(x):
            return True
        else:
            return False
