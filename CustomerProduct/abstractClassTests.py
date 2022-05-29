from gear import *
from clothing import *
from productList import *


# this is the only new test
# don't forget to comment out the shipping charge in one of the derived classes too
def testShippingCharge():
    try:
        # I shouldn't be able to do this because product is now abstract
        p1 = Product(1, "T100", "This is a test product", 100, 10)
        p2 = Product(2, "T200", "This is a test product", 100, 10)
    except TypeError as tErr:
        print(f"Testing creation of abstract product objects.  Expecting a TypeError {tErr}")

    c1 = Clothing(3, "C100", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    c2 = Clothing(4, "C200", "Running tights", 69.99, 3, "pants", "Lucy", "womens", "large", "blue")
    g1 = Gear(5, "G100", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    g2 = Gear(6, "G200", "Sky 10 Kayak", 1049, 2, "paddle", "Eddyline", "plastic laminate", 32)
    pList = ProductList()
    # this is an example of polymorphism.  I can put any kind of product in a product list.
    # can't add products to the list because product is now abstract
    # pList.append(p1)
    # pList.append(p2)
    pList.append(c1)
    pList.append(c2)
    pList.append(g1)
    pList.append(g2)

    print("Testing product list with gear and clothing. Notice the shippingCharge for each product")
    for p in pList:
        print(p)

    print(f"Testing shippingCharge on the list too {pList.shippingCharge}")


