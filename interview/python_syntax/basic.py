#All variables defined on the class level in Python are considered static
class Example:
    Variable = 2           # static variable

print Example.Variable     # prints 2   (static variable)

# Access through an instance
instance = Example()
print instance.Variable    # still 2  (ordinary variable)


# Change within an instance 
instance.Variable = 3      #(ordinary variable)
print instance.Variable    # 3   (ordinary variable)
print Example.Variable     # 2   (static variable)


# Change through Class 
Example.Variable = 5       #(static variable)
print instance.Variable    # 3  (ordinary variable)
print Example.Variable     # 5  (static variable)