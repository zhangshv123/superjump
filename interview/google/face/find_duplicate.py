#!/usr/bin/python
"""
A bunch of information to the user,the name , email address and phone number
asked to repeat the user to return in groups .
the name, email and phone number three there is a repeat of the same.
the problem is a connection diagram .
"""
from collections import defaultdict


class User:

    def __init__(self, name, phone, address):
        """
        constructor function
        :type name: str
        :type name: str
        :address: str
        """
        self.name = name
        self.phone = phone
        self.address = address

    def __lt__(self, other):
        """
        override compare function
        :type other: User
        """
        if self.name != other.name:
            return self.name < other.name
        if self.phone != other.phone:
            return self.phone < other.phone
        if self.address != other.address:
            return self.address < other.address
        return False

#    def __eq__(self, other):
#        """
#        override equal function
#        :type other: User
#        """
#        if self.name == other.name:
#            return True
#        if self.phone == other.phone:
#            return True
#        if self.address == other.address:
#            return True
#        return False

    def is_duplicate(self, other):
        """
        override equal function
        :type other: User
        """
        if self.name == other.name:
            return True
        if self.phone == other.phone:
            return True
        if self.address == other.address:
            return True
        return False


class Solution:
    def find_duplicate(self, users):
        if users is None or len(users) < 2:
            return []
        users.sort()
        dup_users = []
        if users[0].isDuplicate(users[1]):
            dup_users.append(users[0])
        for index, user in enumerate(users[1:]):
            if user.isDuplicate(users[index - 1]):
                dup_users.append(user)
        return dup_users

    def find_union(self, users):
        parent_d = defaultdict()
        for user in users:
            parent_d[user] = user
        for index_1, user1 in enumerate(users):
            for index_2, user2 in enumerate(users[index_1 + 1:]):
                self.union(user1, user2, parent_d)
        roots = filter(lambda key: parent_d[key] == key, parent_d.keys())
        return roots

    def union(self, user1, user2, parent_d):
        root1 = self.find_uion_helper(user1, parent_d)
        root2 = self.find_uion_helper(user2, parent_d)
        if root1 != root2 and root1.is_duplicate(root2):
            parent_d[root1] = root2
            return True
        return False

    def find_uion_helper(self, user, parent_d):
        while user != parent_d[user]:
            user = parent_d[user]
        return user
