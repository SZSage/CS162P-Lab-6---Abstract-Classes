from productBest import *


class Gear(Product):
    """ Gear "is a" Product.  Inheritance relationship.
    Product is the base class.  Gear is the derived class.
    """

    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0, sport="na", brand="na", feature="na",
                 weight=0):
        # constructor for a derived class will often call the constructor for the base class.
        # super() is the function that returns the parent or base or super class
        super().__init__(id, code, description, unitPrice, quantity)
        # attributes that a gear object will have
        # these are in addition to the attributes in a product object
        # NOTE:  brand is in both Gear and Clothing.  Which means it probably should have been in Product.
        # I didn't want to change the Product implementation
        self.__sport = sport
        self.__brand = brand
        self.__feature = feature
        self.__weight = weight

    # here's the implementation of the abstract property getter.  Notice that the heading has to match exactly.
    # if you comment this property out, when you try to create a gear object you'll get a TypeError
    @property
    def shippingCharge(self):
        return 1 * self.__weight

    # property procedures.  There's nothing new here.
    # Notice that a gear object has 9 properties.   5 are defined in Product.
    # Only the gear specific properties are defined here
    @property
    def sport(self):
        return self.__sport

    @sport.setter
    def sport(self, sport):
        # there should be some validation here but I trust that you know how to do that
        self.__sport = sport

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, feature):
        self.__feature = feature

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    # Replace version in Product with gear specific version
    def __str__(self):
        return f'Gear(id: {self.id}, code: {self.code}, description: {self.description}, ' \
               f'unit price: {self.unitPrice}, quantity: {self.quantity}, ' \
               f'sport: {self.__sport}, brand: {self.__brand}, feature: {self.__feature}, weight: {self.__weight} ' \
               f'shippingCharge:  {self.shippingCharge})'

    # Replace version in Product with gear specific version
    def __eq__(self, other):
        if other is None or type(self) != type(other):
            return False
        else:
            # start by calling the product version of eq and then look at gear specific attributes
            return (super().__eq__(other) and
                    self.sport == other.sport and self.brand == other.brand and
                    self.feature == other.feature and self.weight == other.weight)
