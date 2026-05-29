class Player:
    def __init__(self, name, credit, age, No):
        self.name = name
        self.credit = credit
        self.age = age
        self.No = No
        self.level = ""
        self.setLevel()

    def getNo(self):
        return self.No
    def getNameByNo(self,No):
        if No==self.No:
            return self.name
    def setNo(self, No):
        self.No = No

    def setTeam(self, name):
        self.team = name

    def getTeam(self):
        return self.team

    def setLevel(self):
        if self.credit >= 0 and self.credit < 1000:
            self.level = "Edge"
        elif self.credit >= 1000 and self.credit < 1500:
            self.level = "Common"
        elif self.credit >= 1500 and self.credit < 2000:
            self.level = "Core"
        elif self.credit >= 2000:
            self.level = "All Star"

    def updateCredit(self, credit):
        self.credit += credit
        self.setLevel()

    def update(self, name, credit, age, No):
        self.name = name
        self.credit = credit
        self.age = age
        self.No = No
        self.setLevel()

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit

    def getLevel(self):
        return self.level

    def hasName(self, name):
        return self.getName().lower() == name.lower().strip()
