courses = [ "MIT","Cybersecurity","Data Science"]
print(courses)
#Accessing an element
print(courses[2])

# Looping thru an array
for x in courses:
    print("Course is",x)

# adding a new element to an array
courses.append("Laravel")
print(courses)

# Removing an element
courses.remove("Cybersecurity")
