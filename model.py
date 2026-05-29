from Teams import Teams
from Team import Team
from Players import Player
from Validator import Validator

class Model:
    def __init__(self):
        self.teams = Teams()
        self.validator = Validator()
    
    def get_teams(self):
        return self.teams.getTeams()
    
    def add_team(self, name):
        new_team = Team(name)
        new_team.credit = 0.0
        new_team.age = 0
        new_team.no = 0
        
        self.teams.addTeam(new_team)

    def team_exists(self, name):
        for team in self.teams.getTeams():  
            if team.getName().lower() == name.lower().strip():  
                return True
        return False
    
    def deleteTeam(self, name):
        for team in self.teams.getTeams():
            if team.getName().lower() == name.lower().strip():
                self.teams.getTeams().remove(team)
                break
       
    def get_team_by_name(self, name):
        for team in self.teams.getTeams():
            if team.hasName(name):
                return team
        return None
    
    def add_player_to_team(self, team_name, player_name, player_credit, player_age, player_no):
        team = self.get_team_by_name(team_name)
        if team:
            player_credit = int(player_credit)
            new_player = Player(player_name, player_credit, player_age, player_no)
            team.addPlayer(new_player)
            print(f"Player {player_name} added to team {team_name} successfully.")
            return True
        else:
            print(f"Team {team_name} not found.")
            return False
        
    def update_player(self, team_name, old_player_name, new_player_name, new_player_credit, new_player_age, new_player_no):
        team = self.get_team_by_name(team_name)
        if team:
            players = team.getPlayers()
            for player in players:
                if player.getName().lower() == old_player_name.lower().strip():
                    player.name = new_player_name
                    player.credit = new_player_credit
                    player.age = new_player_age
                    player.number = new_player_no
                    print(f"Player {old_player_name} in team {team_name} updated successfully.")
                    return True
            print(f"Player {old_player_name} not found in team {team_name}.")
            return False
        else:
            print(f"Team {team_name} not found.")
            return False
    
    def deletePlayer(self, name, player_name):
        team = self.get_team_by_name(name)
        if team:
            players = team.getPlayers()
            for player in players:
                if player.getName().lower() == player_name.lower().strip():
                    players.remove(player)
                    break