from Team import Team
from Player import Player
class Teams:
    def __init__(self):
        self.teams=[]
        self.teams.append(Team("Suns"))
        self.teams.append(Team("Bulls"))
        self.teams.append(Team("Hawks"))
        self.teams.append(Team("Nets"))
        self.TeamInit()

    def TeamInit(self):
        for t in self.teams:
            if t.getName() == "Suns":
                t.getPlayers().append(Player("Devin Booker", 2500.0, 26, 1))
                t.getPlayers().append(Player("Chris Paul", 1500.0, 37, 3))
                t.getPlayers().append(Player("Deandre Ayton", 2000.0, 24, 22))
                t.getPlayers().append(Player("Kevin Durant", 3000.0, 34, 35))
                t.getPlayers().append(Player("Terrence Ross", 1000.0, 32, 8))
                for player in t.getPlayers():
                    player.setTeam(t.getName())
            elif t.getName() == "Bulls":
                t.getPlayers().append(Player("Andre Drummond", 1500.0, 29, 3))
                t.getPlayers().append(Player("Zach LaVine", 3000.0, 28, 8))
                t.getPlayers().append(Player("Dalen Terry", 900.0, 20, 25))
                t.getPlayers().append(Player("Terry Taylor", 1000.0, 23, 32))
                t.getPlayers().append(Player("Carlik Jones", 800.0, 25, 22))
                for player in t.getPlayers():
                    player.setTeam(t.getName())
            elif t.getName() == "Hawks":
                t.getPlayers().append(Player("Trae Young", 2200.0, 24, 11))
                t.getPlayers().append(Player("John Collins", 2000.0, 25, 20))
                t.getPlayers().append(Player("Aaron Holiday", 800.0, 26, 3))
                t.getPlayers().append(Player("Jalen Johnson", 1000.0, 21, 1))
                t.getPlayers().append(Player("Trent Forrest", 1200.0, 24, 2))
                for player in t.getPlayers():
                    player.setTeam(t.getName())
            elif t.getName() == "Nets":
                t.getPlayers().append(Player("Mikal Bridges", 2400.0, 26, 1))
                t.getPlayers().append(Player("Ben Simmons", 2000.0, 26, 10))
                t.getPlayers().append(Player("Patty Mills", 900.0, 34, 8))
                t.getPlayers().append(Player("Joe Harris", 1200.0, 31, 12))
                t.getPlayers().append(Player("Seth Curry", 1900.0, 32, 30))
                for player in t.getPlayers():
                    player.setTeam(t.getName())

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def hasName(self, name):
        return self.name == name

    def getTeams(self):
        return self.teams

    def addTeam(self, team):
        self.teams.append(team)
