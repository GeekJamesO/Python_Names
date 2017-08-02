# Assignment: Names
# Write the following function.
#
# Part I
    # Given the following list:
    #
    # students = [
    #      {'first_name':  'Michael', 'last_name' : 'Jordan'},
    #      {'first_name' : 'John', 'last_name' : 'Rosales'},
    #      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    #      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    # ]
    # Copy
    # Create a program that outputs:
    #
    # Michael Jordan
    # John Rosales
    # Mark Guillen
    # KB Tonel

def Names_I(PeopleArray):
    for person in PeopleArray:
        print("{0} {1}".format(person['first_name'], person['last_name'] ))

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
     ]

print "Function Names_I"
print "Inputs: {0}".format(students)
print ""
Names_I(students)
print ""


# Part II
    # Now, given the following dictionary:
    #
    # users = {
    #  'Students': [
    #      {'first_name':  'Michael', 'last_name' : 'Jordan'},
    #      {'first_name' : 'John', 'last_name' : 'Rosales'},
    #      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    #      {'first_name' : 'KB', 'last_name' : 'Tonel'}
    #   ],
    #  'Instructors': [
    #      {'first_name' : 'Michael', 'last_name' : 'Choi'},
    #      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    #   ]
    #  }
    # Create a program that prints the following format (including number of
    # characters  in each combined name):
    #
    # Students
    # 1 - MICHAEL JORDAN - 13
    # 2 - JOHN ROSALES - 11
    # 3 - MARK GUILLEN - 11
    # 4 - KB TONEL - 7
    # Instructors
    # 1 - MICHAEL CHOI - 11
    # 2 - MARTIN PURYEAR - 13
#
# Note: The majority of data we will manipulate as web developers will be hashed
# in a dictionary using key-value pairs. Repeat this assignment a few times to
# really get the hang of unpacking dictionaries, as it's a very common requirement
# of any web application.


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def Names_II( TheUsers ):
    for category in TheUsers.keys():
        print category
        for person in TheUsers[category]:
            print "{0} {1} - {2}".format(person["first_name"],person["last_name"], len(person["first_name"]) + len(person["last_name"] ) )

print "Function Names_II"
print "Inputs: {0}".format(users)
print ""
Names_II(users)
