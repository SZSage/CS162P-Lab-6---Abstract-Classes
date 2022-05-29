from productBest import *


class Clothing(Product):
    """ Clothing "is a" Product.  Inheritance relationship.
    Product is the base class.  Clothing is the derived class.
    """

    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0,
                 category="na", brand="na", gender="na", size="na", color="na"):
        # constructor for a derived class will often call the constructor for the base class.
        # super() is the function that returns the parent or base or super class
        super().__init__(id, code, description, unitPrice, quantity)
        # attributes that a clothing object will have
        # these are in addition to the attributes in a product object
        # NOTE:  brand is in both Gear and Clothing.  Which means it probably should have been in Product.
        # I didn't want to change the Product implementation
        self.__category = category
        self.__brand = brand
        self.__gender = gender
        self.__color = color
        self.__size = size

    # here's the implementation of the abstract property getter.  Notice that the heading has to match exactly.
    # if you comment this property out and try to create a clothing object, you'll get a TypeError
    @property
    def shippingCharge(self):
        return 1

    # property procedures.  There's nothing new here.
    # Notice that a clothing object has 10 properties.   5 are defined in Product.
    # Only the clothing specific properties are defined here
    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        # there should be some validation here but I trust that you know how to do that
        self.__category = category

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    # Replace or override version in Product with clothing specific version
    def __str__(self):
        return f'Clothing(id: {self.id}, code: {self.code}, description: {self.description}, ' \
               f'unit price: {self.unitPrice}, quantity: {self.quantity}, ' \
               f'category: {self.__category}, gender: {self.__gender}, brand: {self.__brand}, ' \
               f'color: {self.__color}, size: {self.__size} shipping charge: {self.shippingCharge})'

    # Replace or override version in Product with clothing specific version
    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        else:
            # start by calling the product version of eq and then look at gear specific attributes
            return (super().__eq__(other) and
                    self.category == other.category and self.brand == other.brand and
                    self.gender == other.gender and self.color == other.color and self.size == other.size)
