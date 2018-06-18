"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""

"""
Just go through all pairs of numbers a and b and replace them with a+b, a-b, a*b and a/b, . 
Use recursion for the now smaller list. Positive base case is the list being [24] (or close enough).

I prevent division-by-zero by using b and a/b instead of just a/b. If b is zero, then b and a/b is zero. 
And it’s ok to have that zero, since a*b is zero as well. It’s not even a second zero, because I’m creating 
a set of the up to four operation results, so duplicates are ignored immediately.

Oh and note that I’m using Python 3, so / is “true” division, not integer division like in Python 2. 
And it would be better to use fractions.Fraction instead of floats. I actually just realized that 
there is in fact an input where simple floats fail, namely [3, 3, 8, 8]. Floats calculate 
23.999999999999989341858963598497211933135986328125 instead of 24. It’s not in the judge’s test suite, 
but it should be soon (Edit: it now is). Using Fraction however made my solution exceed the time limit,
so I settled for the above approximation solution.
"""

def judgePoint24(self, nums):
    if len(nums) == 1:
        return math.isclose(nums[0], 24)
    return any(self.judgePoint24([x] + rest)
               for a, b, *rest in itertools.permutations(nums)
               for x in {a+b, a-b, a*b, b and a/b})