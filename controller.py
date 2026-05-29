class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)
        self.selected_team_name = None
   
    def get_allPlayer_info(self):
        all_player_info = []
        teams = self.model.get_teams()
        for team in teams:
            players = team.getPlayers()
            for player in players:
                player_info = {
                    'Team': team.getName(),
                    'Player Name': player.getName(),
                    'Player Credit': player.getCredit(),
                    'Player Age': player.getAge(),
                    'Player No': player.getNo(),
                    'Player Level': player.getLevel()
                }
                all_player_info.append(player_info)
        return all_player_info
    
    def filter_players(self, level_filter, name_filter, age_filter_from, age_filter_to):
        all_players_info = self.get_allPlayer_info()
        filtered_players = []

        for player_info in all_players_info:
            include_player = True
            if level_filter and player_info['Player Level'] != level_filter:
                include_player = False
                
            if name_filter and name_filter.lower() not in player_info['Player Name'].lower():
                include_player = False

            if age_filter_from and age_filter_to:
                try:
                    age_from = int(age_filter_from)
                    age_to = int(age_filter_to)
                    player_age = player_info['Player Age']
                    if player_age < age_from or player_age > age_to:
                        include_player = False
                except ValueError:
                    include_player = False

            if include_player:
                filtered_players.append(player_info)
            
        if not filtered_players:
            self.view.update_view_players_label("Players list is not loaded")
        else:
            self.view.update_players_window(filtered_players)

        return filtered_players

    
    def get_team_info(self):
        teams_info = []
        for team in self.model.get_teams():
            team_info = {
                'Team Name': team.getName(),
                'Number of Players': team.CountPlayer(),
                'Average Player Credit': team.CountAvgCredit(),
                'Average Age': team.CountAvgAge()
            }
            teams_info.append(team_info)
        return teams_info 

    def add_new_team(self, name):
        if self.model.team_exists(name):
            self.view.show_error_message(f"{name} Team already exists")
            return
    
        self.model.add_team(name)
        teams_info = self.get_team_info()
        self.view.update_team_table(teams_info)
    
    def deleteTeam(self,team_name):
        self.model.deleteTeam(team_name)
        teams_info = self.get_team_info()
        self.view.update_team_table(teams_info)
    
    def manage_team(self, team_name):
        if self.counterWin < 1000:
            self.view.manageTeam(team_name)
    
    def get_player_info(self, team_name):
        team = self.model.get_team_by_name(team_name)
        if team:
            players_info = []
            players = team.getPlayers()
            if players: 
                for player in players:
                    player_info = {
                        'Player Name': player.getName(),
                        'Player Credit': player.getCredit(),
                        'Player Age': player.getAge(),
                        'Player No': player.getNo()
                    }
                    players_info.append(player_info)
                return players_info
    
    def add_new_player(self, name, player_name,player_credit, player_age, player_no):
        self.model.validator.clear()
        self.model.validator.generateErrors(player_name,player_credit, player_age, player_no)
        
        if self.model.validator.errors:
            error_message = "\n".join(self.model.validator.errors)
            self.view.show_error_message1(error_message)
            return
        
        self.model.add_player_to_team(name, player_name, player_credit, player_age, player_no)
        team_name = self.set_selected_team_name
        player_info = self.get_player_info(team_name)
        new_player_credit = int(new_player_credit)
        self.view.update_player_table(player_info)
        
    def set_selected_team_name(self, team_name):
        self.selected_team_name = team_name
    
    def update_player(self, team_name, old_player_name, new_player_name, new_player_credit, new_player_age, new_player_no):
        if self.view.selected_player:
            success = self.model.update_player(team_name, old_player_name, new_player_name, new_player_credit, new_player_age, new_player_no)
            if success:
                self.view.updatePlayerWindow.destroy()
        else:
            print("No player selected to update.")
        
    def deletePlayer(self, team_name, player_name):
        self.model.deletePlayer(team_name, player_name)
        player_info = self.get_player_info(team_name)
        self.view.update_player_table(player_info)    
    
    def get_round_results(self):
        pass