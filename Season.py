from Record import Record
from Game import Game
class Session:
    def __init__(self):
        self.schedule = []
        self.current = []
        self.records=[]
        self.round = 0

    def addTeams(self, teams):
        g = Game(len(self.schedule) + 1)
        g.add(teams[0])
        g.add(teams[1])
        self.schedule.append(g)
        self.current.remove(teams)

    def initialiseSeason(self, teams):
        self.current  = []
        self.round = 0
        self.records = []
        for team in teams.getTeams():
            self.current.append(team)

    def play(self, round):
            result = ""
            Win = []
            Lost = []
            result = []
            for g in self.schedule:
                for t in g.play():
                    result.append(t)
                Win.append(result[0])
                Lost.append(result[1])
                result.clear()
            self.current.extend(Win)
            for i in range(len(Win)):
                self.records.append(Record(Win[i].getName(), Lost[i].getName(), i, round))
            result += "All games finished! You can use 4 to check the results.\n"
            if len(self.current) == 1:
                result += "This season ends!\n"
                result += f"{self.current[0].getName()} is the Champion!!\n"

    def play_round(self):
        self.round += 1
        self.play(round)