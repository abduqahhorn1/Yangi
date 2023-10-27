import random

class War:

    def attack(self,target, bullet=3):
        bullets = random.randint(1, bullet)
        damage = bullets * self._damage
        print(f"{self.name} {target.name} ga hujumga o'tdi")
        print(f"{target.name} ga {bullets} ta o'q tegdi ")
        if target.defence() == 0:
            target.life -= damage
        else:
            print(f"{target.name} ximoyalanishga ulgurdi")
        print(f"{target.name} ning joni {target.life}% qoldi")


    def defence(self, ):
        return random.randint(0,1)