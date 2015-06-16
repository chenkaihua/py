#!/usr/bin/python
import os

words = {}
words["Hello"] = "Bonjour"
words["Yes"] = "Oui"
words["No"] = "Non"
words["Bye"] = "Au Revoir"
words["sentence"] = "Hello/nPython"

print words            # print key-pairs.
del words["Yes"]       # delete a key-pair.
print words            # print key-pairs.
words["Yes"] = "Oui!"  # add new key-pair.
print words            # print key-pairs.
print words["Bye"],words["Yes"]
print words["sentence"]

items = [ "Abby","Brenda","Cindy","Diddy" ]
print "items is", items
for i in items:
    print i

#print platform
from random import *

print random ()
print randint (1, 100)
x = randint(20, 50)
print "x=",x

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)
print items

dir(os)
os.getcwd()
os.chdir('/tmp')
os.system('mkdir today')
x = 3
if x < 10:
    print 'x is smaller that 10'
else:
    print 'x is larger than 10'

if os.path.isfile('abc.txt'):
    print "abc.txt is existed"
else:
    print 'abc isnt existed'

