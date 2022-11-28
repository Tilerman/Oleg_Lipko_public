#16.9.1
class MagicStr():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"MagicStr: {self.x},{self.y},{self.width},{self.height}"
#16.9.2
class прямоугольник():
    def __init__(self, ширина, длина):
        self.ширина = ширина
        self.длина = длина
    def get_площадь(self):
        return self.ширина * self.длина
#16.9.3
class Client():
    def __init__(self, firstname,secondname, city, balance):
        self.firstname = firstname
        self.secondname = secondname
        self.city = city
        self.balance = balance
    def get_client(self):
        return f"{self.firstname} {self.secondname}. {self.city}. Баланс: {self.balance} руб."
#16.9.4
    def get_corporativ_client(self):
        return f"{self.firstname} {self.secondname}, {self.city}"
