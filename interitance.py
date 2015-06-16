class User:

    name = ""
    def __init__(self, name):
       self.name = name

    def printName(self):
       print "Name  = " + self.name
 
brian = User("brian")
brian.printName()

class Programmer(User):
 
    def __init__(self, name):
                self.name = name
    def doPython(self):
            print "Programming Python"

brian = User("brian")
brian.printName()
 
diana = Programmer("Diana")
diana.printName()
diana.doPython()

def f(x,y):
    print 'You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y)
    print 'x * y = ' + str(x*y)

f(3,2)
