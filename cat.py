class Cat():
    def __init__(self, name = "", type_animal = "", sex = "", breed = "", age = 0, reg_number = "", status = ""):
        self.name = name
        self.type_animal = type_animal
        self.sex = sex
        self.breed = breed
        self.age = age
        self.reg_number = reg_number
        self.status = status
    def getName(self):
        return self.name
    def getType_animal(self):
        return self.type_animal
    def getSex(self):
        return self.sex
    def getBreed(self):
        return self.breed
    def getAge(self):
        return self.age
    def getReg_number(self):
        return self.reg_number
    def getStatus(self):
        return self.status
