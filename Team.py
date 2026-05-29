from Players import Players
class Team:
    def __init__(self,name):
        self.name=name
        self.players=Players()
    def getName(self):
        return self.name
    def getPlayers(self):
        return self.players.getCurrentList()
    def getCurrentList(self):
        return self.players
    def hasName(self, name):
        return self.getName().lower() == name.lower().strip()
    def CountPlayer(self):
        return self.players.getPlayerNumber()
    def CountAvgAge(self):
        return self.players.CountAvgAge()
    def CountAvgCredit(self):
        return self.players.CountAvgCredit()
