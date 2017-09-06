print "Assignment: Names"
print " Part I"
print "   Create a program that outputs first and then last name."
print "  "
def printName(arr):
    for person in arr:
        print "    {} {}".format(person['first_name'], person['last_name'])

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
printName(students)

print "Part II"
print "Now, given the following dictionary:"
print " "
print "Create a program that prints the following format (including number of characters in each combined name):"
print " "

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

def printName_2(arr):
    counter = 0
    for person in arr:
        counter += 1
        print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], len(person['first_name']) + len(person['last_name']))

def printRolesAndUsers(doubleArray):
    for key in doubleArray:
        print key
        printName_2(doubleArray[key])
    print " "

printRolesAndUsers(users)
