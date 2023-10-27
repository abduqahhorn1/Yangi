class Phone:
    def __init__(self, model, room, price, color):
        self.model = model
        self.room = room
        self.price = price
        self.color = color

phone1 = Phone("iPhone 12", "Xotira 256Gb", "Narxi 650$", "Rangi: Black")

print(phone1.model)  
print(phone1.room)  
print(phone1.price) 
print(phone1.color)  