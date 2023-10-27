from hero import Hero
from war import War
class Human(Hero,War):
    def __init__(self, name: str, rank: str, Life: int):
        super().__init__(name, rank, Life)
        self._damage = 1

class Alian(Hero,War):
    def __init__(self, name: str, rank: str, Life: int):
        super().__init__(name, rank, Life)
        self._damage = 3

a = Alian(name="Mukambu", rank="Zod-12" , Life=70)
h = Human(name="Teshavoy", rank="Praporshik" , Life=100)

a.attack(target=h , bullet=10)


