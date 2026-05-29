class Game:
    def __init__(self, term):
        self.teams = []
        self.results = []
        self.result = ""
        self.term = term

    def size(self):
        return len(self.teams)

    def add(self, e):
        self.teams.append(e)

    def get(self):
        return self.teams

    def setResult(self, s):
        self.result = s

    def getResult(self):
        return self.result

    def play(self):
        firstTeam = self.teams[0].getCurrentList().CountAvgCredit()
        secondTeam = self.teams[1].getCurrentList().CountAvgCredit()

        if firstTeam > secondTeam:
            diff = (firstTeam - secondTeam) / 5.0
            for p in self.teams[0].getPlayers():
                p.updateCredit(diff)
                self.results.append(self.teams[0])
                self.results.append(self.teams[1])
            for p in self.teams[1].getPlayers():
                p.updateCredit(-diff)
            self.setResult(self.teams[0].getName() + "wins")
        else:
            self.results.append(self.teams[1])
            self.results.append(self.teams[0])
            diff = (secondTeam - firstTeam) / 5.0
            for p in self.teams[0].getPlayers():
                p.updateCredit(-diff)
            for p in self.teams[1].getPlayers():
                p.updateCredit(diff)
            self.setResult(self.teams[1].getName() + "wins")

        return self.results
