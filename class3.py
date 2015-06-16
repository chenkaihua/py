#!/usr/bin/env python

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(std):
        print('%s, %s' % (std.name, std.score))
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

if __name__=='__main__':
    bart = Student('Bart Simpson', 59)
    bart.print_score()
    result = bart.get_grade()
    print result
