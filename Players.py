from Player import Player
class Players:
    def __init__(self):
        self.Players = []

    def addPlayer(self, player):
        self.Players.append(player)
        
    def removePlayer(self, player):
        self.Players.remove(player)

    def hasPlayer(self, name):
        for e in self.Players:
            if e.hasName(name) and name.strip() != "":
                return True
        return False

    def getPlayer(self, name):
        for p in self.Players:
            if p.hasName(name):
                return p
        return None

    def remove(self, selectedItems):
        for selectedItem in selectedItems:
            self.Players.remove(selectedItem)

    def addPlayers(self, selectedItems):
        self.Players.extend(selectedItems)

    def getCurrentList(self):
        return self.Players

    def getPlayerNumber(self):
        return len(self.Players)

    def CountAvgCredit(self):
        sum = 0
        for p in self.Players:
            sum = sum + p.getCredit()
        if sum==0:
            return 0
        else:
            return sum / len(self.Players)

    def CountAvgAge(self):
        sum = 0
        for p in self.Players:
            sum = sum + p.getAge()
        if sum == 0:
            return 0
        else:
            return sum / len(self.Players)