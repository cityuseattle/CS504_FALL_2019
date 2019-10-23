courses = ('CS101', 2.0, 3)
#tuples don't take assignment to indicies, but I can just replace a tuple with a new one that has the change I want.
courses = courses[0], 4.0, courses[2]
print(courses)