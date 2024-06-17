# abstraction in python
# from abc import ABC,abstractmethod

# abstract class
class Subject():
    # @abstractmethod
    def subject(self):
        pass

class Maths(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Maths")

class Physics(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Physics")

class Chemistry(Subject):
    # override superclass method
    def subject(self):
        print("Subject is Chemistry")

class English(Subject):
    # override superclass method
    def subject(self):
        print("Subject is English")

maths=Maths()
maths.subject()

physics=Physics()
physics.subject()

chemistry=Chemistry()
chemistry.subject()

english=English()
english.subject()