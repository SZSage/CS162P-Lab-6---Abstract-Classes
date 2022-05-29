# the abc module contains the ABC "helper" class from which all abstract classes should be derived
# and decorators like abstractmethod and abstract property
from abc import ABC, abstractmethod


# Product is now derived from ABC which makes it an abstract class
# and abstract class is used as part of the infrastructure of other classes
# and contains one or more abstract methods or properties
# an abstract class is a "building block" but can NOT be instantiated
class Product(ABC):
    """ This class represents a product.  It adds validation to the property setters."""

    def __init__(self, id=0, code="na", description="na", unitPrice=0, quantity=0):
        self.__id = id
        self.__code = code
        self.__description = description
        self.__unitPrice = unitPrice
        self.__quantity = quantity

    # the product class can not implement the shippingCharge property because
    # shipping rules are different for clothing and gear
    # adding this definition here requires concrete derived classes to implement the property
    @property
    @abstractmethod
    def shippingCharge(self):
        pass

    # nothing else in this class has changed
    @property
    def id(self):
        return self.__id

    @property
    def code(self):
        return self.__code

    @property
    def description(self):
        return self.__description

    @property
    def unitPrice(self):
        return self.__unitPrice

    @property
    def quantity(self):
        return self.__quantity

    @id.setter
    def id(self, id):
        if isinstance(id, int) and id > 0: # it's valid for a programmer to call p.id = 10
            self.__id = id
        else: # but invalid to use a non-integer value or a value that's < 0
            raise ValueError(f"Id must be a non-zero positive integer. {type(id)}  {id}") # this error cannot be ignored in the calling code

    @code.setter
    def code(self, code):
        if isinstance(code, str) and len(code) == 4:
            self.__code = code
        else:
            raise ValueError(f"Code must a 4 character string {type(code)}  {code}")

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description.strip()) > 0:
            self.__description = description.strip()
        else:
            raise ValueError(f"Description must a non-empty character string {type(description)}  {description}")

    @unitPrice.setter
    def unitPrice(self, unitPrice):
        if isinstance(unitPrice, float) and unitPrice >= 0:
            self.__unitPrice = unitPrice
        else:
            raise ValueError(f"Unit price must be a positive number. {type(unitPrice)}  {unitPrice}")

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError(f"Quantity must be a positive number. {type(quantity)}  {quantity}")

    def __str__(self):
        return f'Product(id: {self.__id}, code: {self.__code}, description: {self.__description}, ' \
               f'unit price: {self.__unitPrice}, quantity: {self.__quantity})'

    def __eq__(self, other):
        """ This "magic method" is called when you check the equality of 2 products.  I had to add this to the product class
        in order for find and __contains__ to work"""
        if isinstance(other, Product):
            return (self.id == other.id and self.code == other.code and
                    self.description == other.description and self.unitPrice == other.unitPrice and
                    self.quantity == other.quantity)
        else:
            return False



