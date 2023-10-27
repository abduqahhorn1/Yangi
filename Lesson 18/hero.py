from war import War

class Hero(War):
    def __init__(self, name:str, rank:str, life:int):
        self.name = name
        self.rank = rank
        self.life = life