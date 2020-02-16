from random import randint
   


class Proizvod:
    def __init__(self, name, basicPrice, quantity):
        self.name = name
        self.basicPrice = basicPrice
        self.quantity = quantity
    def getPDVPercent(self):
        return 0.25
    def getTotalPrice(self):
        return self.basicPrice * self.quantity * ( 1 + self.getPDVPercent())
    def __str__(self):
        return "[Ime: {}, BasicPrice: {}, Quantity: {}]".format(self.name, self.basicPrice, self.quantity)
    def __repr__(self):
        return self.__str__()

class Sok(Proizvod):
    def getPDVPercent(self):
        return 0.20 
class Jabuka(Proizvod):
    def getPDVPercent(self):
        return 0.10
class Kruh(Proizvod):
    pass    
class Cokolada(Proizvod):
    pass

PRODUCT_NUM = 100

functions = [Jabuka, Sok, Kruh, Cokolada]

def nextProizvod():
    for i in range(PRODUCT_NUM):
        name = chr(ord('a') + randint(0, 26))
        basicPrice = randint(4, 40)
        quantity = randint(4,40)
        object = functions[randint(0, len(functions) - 1)]
        yield object(name, basicPrice, quantity)

rez = 0  

for proizvod in nextProizvod():
    print(proizvod)
    rez +=  proizvod.getTotalPrice()
    
print("Ukupna cijena: {}".format(rez))


