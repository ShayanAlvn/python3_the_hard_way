#ex44
class Parent(object):

    def override(self):
        print("parent override()")

    def implicit(self):
        print("parent implicit()")

    def altered(self):
        print("parent altered()")


class Child(Parent):

    def override(self):
        print("child override")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()