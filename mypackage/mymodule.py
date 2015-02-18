""" Module containing a silly example of OOP """

class Animal:
    """ Superclass defining an animal """

    def __init__(self, name):
        """Constructs an animal"""

        # instance attributes
        self.name = name
        self.last_ate = None

        print("Created new animal named " + name)

    def eat(self, food ):
        """ Don`t let your little guy starve!

        :param food: Nom Nom

        """
        self.last_ate = food
        print(self.name + " noms on " + self.last_ate)

    def poop(self):
        """ Sometimes...

        :return: Better pick this up!

        """
        print(self.name + " poops!!!")
        self.last_ate = None
        return 'That was once ' + self.last_ate


class Dog(Animal):
    """ Cute little dog """
    def __init__(self, name='poor little buddy has no name'):
        # Call to parent init:
        super(Dog, self).__init__(name)
        # instance attributes
        self.tricks = set([])

    def is_really_smart(self):
        """ Checks if the dof has offspring """
        return bool(self.tricks)

    def teach(self, trick):
        self.tricks.add(trick)


class Cat(Animal):
    """ Super cute cat! """
    def __init__(self, name, color):
        # Call to parent init:
        super(Cat, self).__init__(name)
        self.color = color


def main():
    bill = Cat("Bill the Cat", "orange and white")
    bill.eat('cat food')

    walter = Dog()
    walter.name = "Walter"
    walter.breed = "Pug"
    walter.eat("pizza")
    walter.poop()

    walter.teach('play dead')
    walter.teach('fetch ball')

    if walter.is_really_smart():
        print('Walter knows ' + ', '.join(walter.tricks))

if __name__ == '__main__':
    main()

