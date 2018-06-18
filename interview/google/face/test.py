#!/usr/bin/python

from find_duplicate import User,Solution

user1 = User("a","123","aa@edu.com")
user2 = User("c","127","ac@edu.com")
user3 = User("c","125","aa@edu.com")
users = [user1, user2, user3]
sol = Solution
#print(user1 == user1)
#print(len(sol.findDuplicate(users)))
for user in sol.findUnion(users):
	print(user.name, user.phone, user.address)