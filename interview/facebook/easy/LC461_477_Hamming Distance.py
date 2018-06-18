#!/usr/bin/python
"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):
    def toBit(self, x):
        """
        Just to explain the parts of the formatting string:

            {} places a variable into a string
            0 takes the variable at argument position 0
            : adds formatting options for this variable (otherwise it would represent decimal 6)
            08 formats the number to eight digits zero-padded on the left
            b converts the number to its binary representation
        """
        return '{0:031b}'.format(x)

    def hammingDistance(self, x, y):
        """
        Make an iterator that aggregates elements from each of the iterables.

        Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. The iterator stops when the shortest input iterable is exhausted. With a single iterable argument, it returns an iterator of 1-tuples. With no arguments, it returns an empty iterator.
        """
        return sum(el1 != el2 for el1, el2 in zip(self.toBit(x), self.toBit(y)))

"""
follow up:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
"""

def totalHammingDistance(self, nums):
    return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))