# Markhus Dammar
# 11/13/19
# This is the class file for the person!

class Person():

    def __init__(self, first, last, age, eye, weight):
        self.first = first
        self.last = last
        self.age = age
        self.eye = eye
        self.weight = weight

    def first(self):
        return "The person's first name is " + self.first

    def last(self):
        return "The person's last name is " + self.last

    def age(self):
        return self.first + self.last + " is " + self.age + " years old."

    def eye(self):
        return self.first + self.last + " has " + self.eye + " colored eyes."

    def weight(self):
        return self.first + self.last + " weighs " + self.weight + " pounds."

    def birthday(self):
        self.age = self.age + 1

    def workout(self):
        self.weight = self.weight + 10
