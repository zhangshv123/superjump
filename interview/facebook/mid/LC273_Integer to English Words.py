"""
onvert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution(object):
    def three_bit(self, item):
        twoBits = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        oneBits = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        Twenties = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        res = []
        if item >= 100:
            res.append(oneBits[item / 100])
            res.append("Hundred")
            item %= 100
        if item >= 10 and item < 20:
            res.append(Twenties[item % 10])
            return res
        if item > 10:
            res.append(twoBits[item / 10])
            item %= 10
        if item > 0:
            res.append(oneBits[item])
        return res
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        threeBits = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion"]
        i= 0
        res = []
        while num > 0:
            bits = self.three_bit(num % 1000)
            if len(bits) > 0:
                res = bits + [threeBits[i]] + res
            num /= 1000
            i += 1
        english = " ".join(res).strip()
        return english if len(english) > 0 else "Zero"