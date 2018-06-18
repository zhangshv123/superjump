"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

"""
# Just turn the clock forwards one minute at a time until you reach a time with the original digits.
from datetime import *

class Solution(object):
    def nextClosestTime(self, time):
        digits = set(time)
        while True:
            time = (datetime.strptime(time, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:
                return time