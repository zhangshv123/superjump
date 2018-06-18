"""
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
思路：
http://tinyurl.com/y84o55k5
1、暴力法：最先想到的就是暴力法，依次验证每一个人，一旦发现该人认识其他人或者有其他人不认识该人，就表明验证失败，开始进入下一个人的验证。虽然大多数情况下可以提前结束第二重循环，但是理论上的时间复杂度还是O(n^2)。但这倒是可以通过所有的测试数据。
2、验证法：题目说明最多有一个celebrity。利用这个信息，我们可以将算法的时间复杂度降低到O(n)：我们首先假定k号是celebrity，然后依次判断i号是否认识k，一旦发现不认识，则说明k号不可能是candidate，而i号则有可能是candidate。我们下面证明一个重要结论，就是如果题目中有一个celebrity，则我们的算法必然可以正确地找出该celebrity：
1）假设这个celebrity是0号，那么由于knows(i, 0) (i > 0)永远会返回true，所以k在整个循环中会保持不变，所以循环结束后k == 0，celebrity被作为candidate找出；
2）假设这个celebrity是m号，并且0 < m < n，那么当i == m的时候，knows(m, k)会返回false，此时k会被赋值为m，而此后knows(i, m) (i > m)都会返回true，所以k的值会保持为m直到循环结束，celebrity依然会被作为candidate正确找出。
由此可见，一旦有一个celebrity，我们在第一次循环的时候就会把它找出来，而第二次循环的时候就会验证通过，所以整个算法就会返回该celebrity。
如果给定的集合中没有celebrity，那么第一次循环返回的candidate在第二次循环的时候就会验证失败，所以整个算法就会返回-1。因此，我们的算法是正确的。
这样做的OP是最少的！！！

GeeksforGeeks上的分析：
http://tinyurl.com/nzmjtga

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        for i in range(n):
            if i == celebrity:
                continue
            if knows(celebrity, i):
                return -1
            if not knows(i, celebrity):
                return -1
        return celebrity