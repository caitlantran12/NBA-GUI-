import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from Validator import Validator
from tkinter.messagebox import showinfo
from turtle import width

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.validator = Validator()
        self.counterWin = 0
        self.configure(bg="black")
        self.controller = None
        self.selected_team_name = None  
        self.selected_player = None
        self.round_number = 1
        self.round_number1 = 1
        self.rounds = []
        self.first_round_completed = False
    
        image = Image.open("/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/NBA_Back.jpg")
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=photo)
        label.image = photo  
        label.grid(row=0, column=0, columnspan=3, sticky=tk.EW)
        
        self.explore_teams = tk.Button(self, text='Explore the Teams', command=lambda:self.exploreTeams(), bg='black', fg='white')
        self.explore_teams.grid(row=1, column=0, rowspan=3, sticky=tk.NSEW)
        
        self.gap_label = tk.Label(self, bg='black')
        self.gap_label.grid(row=1, column=1, rowspan=3)
        
        self.arrange_season = tk.Button(self, text='Arrange a new season', command=lambda:self.arrangeSeason(), bg='black', fg='white')
        self.arrange_season.grid(row=1, column=2, rowspan=3, sticky=tk.NSEW)
        
        self.exit_button = tk.Button(self, text='Exit',  command=lambda:self.exit(), bg='black', fg='white')
        self.exit_button.grid(row=4, column=1, sticky=tk.EW)
        
    def exploreTeams(self):
        if self.counterWin < 1000: 
            self.exploreteam = tk.Toplevel(self)
            self.exploreteam.title("Explore Teams")
            self.exploreteam.configure(bg="black")
            self.exploreteam.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            image1 = Image.open("/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/NBA_Back.jpg")
            photo1 = ImageTk.PhotoImage(image1)
            label = tk.Label(self.exploreteam, image=photo1)
            label.image1 = photo1  
            label.grid(row=0, column=0, columnspan=3, sticky=tk.EW)
            
            self.teams_menu = tk.Button(self.exploreteam, text='Teams Menu',  command=lambda:self.teamsMenu(), bg='black', fg='white')
            self.teams_menu.grid(row=1, column=0, rowspan=3, sticky=tk.NSEW)

            self.gap_label = tk.Label(self.exploreteam, bg='black')
            self.gap_label.grid(row=1, column=1, rowspan=3)
            
            self.view_player = tk.Button(self.exploreteam, text='View Players', command=lambda:self.viewPlayers(), bg='black', fg='white')
            self.view_player.grid(row=1, column=2, rowspan=3, sticky=tk.NSEW)
            
            self.close_button = tk.Button(self.exploreteam, text='Close',  command=self.exploreteam.destroy, bg='black', fg='white')
            self.close_button.grid(row=4, column=1, sticky=tk.EW)
        else:
            print("reached max limit")
    
    def viewPlayers(self):
        if self.counterWin < 1000:
            self.viewPlayers = tk.Toplevel(self)
            self.viewPlayers.title("Players")
            self.viewPlayers.configure(bg="black")
            self.viewPlayers.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            self.viewPlayersLabel = tk.Label(self.viewPlayers, text='All Players',font=("Arial", 22), bg='black', fg='white' )
            self.viewPlayersLabel.grid(row=0, column=0, columnspan=6, sticky=tk.NSEW)
            col =  ('Team', 'Player Name', 'Player Credit', 'Player Age', 'Player No', 'Player Level')
            self.allPlayer = ttk.Treeview(self.viewPlayers, columns=col, show='headings')
            self.allPlayer.grid(row=1, column=0, columnspan=6, sticky=tk.NSEW)
            column_width = 150
            for i, c in enumerate(col):
                self.allPlayer.column(c, width=column_width, anchor=tk.CENTER)
       
            self.allPlayer.heading('Team', text='Team')
            self.allPlayer.heading('Player Name', text='Player Name')
            self.allPlayer.heading('Player Credit', text='Player Credit')
            self.allPlayer.heading('Player Age', text='Player Age')
            self.allPlayer.heading('Player No', text='Player No')
            self.allPlayer.heading('Player Level', text='Player Level')
            
            allPlayer_info = self.controller.get_allPlayer_info()
            for info in allPlayer_info:
                self.allPlayer.insert("", "end", values=(
                    info['Team'],
                    info['Player Name'],
                    info['Player Credit'],
                    info['Player Age'],
                    info['Player No'],
                    info ['Player Level']
                ))
    
                
            self.allPlayer.grid(row=1, column=0, sticky=tk.NSEW)
            
            self.filterLbl = tk.Label(self.viewPlayers, text='Filter', font=("Arial", 22), bg='black', fg='white')
            self.filterLbl.grid(row=2, column=0, columnspan=6, sticky=tk.NSEW)

            self.level_filter_label = tk.Label(self.viewPlayers, text='Filter by Level:', bg='black', fg='white')
            self.level_filter_label.grid(row=3, column=2, sticky=tk.EW, padx=(0, 3))
            self.level_filter_entry = ttk.Combobox(self.viewPlayers, values=['Edge', 'Common', 'Core', 'All Star'])
            self.level_filter_entry.grid(row=3, column=3, sticky=tk.EW, padx=(0,3))
            self.level_filter_entry.bind("<<ComboboxSelected>>", self.apply_filters)

            self.name_filter_label = tk.Label(self.viewPlayers, text='Filter by Name:', bg='black', fg='white')
            self.name_filter_label.grid(row=3, column=4, sticky=tk.EW, padx=(0,3))
            self.name_filter_entry = tk.Entry(self.viewPlayers)
            self.name_filter_entry.grid(row=3, column=5, sticky=tk.EW, padx=(0,3))
            self.name_filter_entry.bind("<KeyRelease>", self.apply_filters)

            self.age_filter_label = tk.Label(self.viewPlayers, text='Filter by Age:', font=("Arial", 17), bg='black', fg='white')
            self.age_filter_label.grid(row=4, column=0, columnspan=6, sticky=tk.NSEW)

            self.age_filter_from_label = tk.Label(self.viewPlayers, text='From:', bg='black', fg='white')
            self.age_filter_from_label.grid(row=5, column=2, sticky=tk.EW, padx=(0, 3))
            self.age_filter_entry_from = tk.Entry(self.viewPlayers)
            self.age_filter_entry_from.grid(row=5, column=3, sticky=tk.EW, padx=(5, 0))

            self.age_filter_to_label = tk.Label(self.viewPlayers, text='To:', bg='black', fg='white')
            self.age_filter_to_label.grid(row=5, column=4, sticky=tk.EW, padx=(0, 3))
            self.age_filter_entry_to = tk.Entry(self.viewPlayers)
            self.age_filter_entry_to.grid(row=5, column=5, sticky=tk.EW, padx=(0, 3))

            self.close_button = tk.Button(self.viewPlayers, text='Close', command=self.viewPlayers.destroy, bg='black', fg='white')
            self.close_button.grid(row=6, column=3, sticky=tk.NSEW)

            
    def teamsMenu(self):
        if self.counterWin < 1000:
            self.teamsmenu = tk.Toplevel(self)
            self.teamsmenu.title("Teams Menu")
            self.teamsmenu.configure(bg="black")
            self.teamsmenu.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            self.menulabel = tk.Label(self.teamsmenu, text='All Teams',font=("Arial", 22) )
            self.menulabel.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
            col =  ('Team Name', 'Number of Players', 'Average Player Credit', 'Average Age')
            self.treeview = ttk.Treeview(self.teamsmenu, columns=col, show='headings')
            self.treeview.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
            column_width = 200
            for i, c in enumerate(col):
                self.treeview.column(c, width=column_width, anchor=tk.CENTER)
       
            self.treeview.heading('Team Name', text='Team Name')
            self.treeview.heading('Number of Players', text='Number of Players')
            self.treeview.heading('Average Player Credit', text='Average Player Credit')
            self.treeview.heading('Average Age', text='Average Age')
     
            teams_info = self.controller.get_team_info()
            for info in teams_info:
                self.treeview.insert("", "end", values=(
                    info['Team Name'],
                    info['Number of Players'],
                    info['Average Player Credit'],
                    info['Average Age']
                ))
                
            self.treeview.grid(row=1, column=0, sticky=tk.NSEW)
           
            self.add_button = tk.Button(self.teamsmenu, text='Add', command=lambda:self.addTeam(), bg='black', fg='white')
            self.add_button.grid(row=2, column=0, sticky=tk.NSEW)

            self.manage_button = tk.Button(self.teamsmenu, text='Manage', command=lambda:self.manageTeam(), state=tk.DISABLED, bg='black', fg='white')
            self.manage_button.grid(row=2, column=1, sticky=tk.NSEW)

            self.delete_button = tk.Button(self.teamsmenu, text='Delete',command=lambda:self.deleteTeam(), state=tk.DISABLED, bg='black', fg='white')
            self.delete_button.grid(row=2, column=2, sticky=tk.NSEW)

            self.close_button = tk.Button(self.teamsmenu, text='Close', command=self.teamsmenu.destroy, bg='black', fg='white')
            self.close_button.grid(row=2, column=3, sticky=tk.NSEW)
            
            self.treeview.bind("<ButtonRelease-1>", self.on_tree_select)
        else:
            print("reached max limit")            
    
    def addTeam(self):
        if self.counterWin < 1000:
            self.addTeam = tk.Toplevel(self)
            self.addTeam.title("Adding New Team")
            self.addTeam.configure(bg="black")
            self.addTeam.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/edit.png')
            
            self.addteamLbl = tk.Label(self.addTeam, text='Team Details',font=("Arial", 16) )
            self.addteamLbl.grid(row=0, column=0,columnspan=1, sticky=tk.E, pady=(10, 5))
            
            tk.Label(self.addTeam, text="Name:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, padx=(10, 5))
            team_name_entry = tk.Entry(self.addTeam, font=("Arial", 12))
            team_name_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
            
            self.add_button = tk.Button(self.addTeam, text='Add', command=lambda:self.add_new_team_and_update_table(team_name_entry.get()),bg='black', fg='white')
            self.add_button.grid(row=2, column=1, sticky=tk.NSEW)
            
        else:
            print("reached max limit")
            
    def add_new_team_and_update_table(self, new_team_name):
        self.controller.add_new_team(new_team_name) 
        teams_info = self.controller.get_team_info()
        self.controller.view.update_team_table(teams_info)
        self.controller.view.addTeam.destroy() 
    
    def deleteTeam(self):
        selected_item = self.treeview.selection()
        if selected_item:
            team_name = self.treeview.item(selected_item)['values'][0]
            self.controller.deleteTeam(team_name)
    
    def manageTeam(self):
        if self.counterWin < 1000 and self.selected_team_name:
            self.manageTeamWindow = tk.Toplevel(self)
            self.manageTeamWindow.title(f"Managing Team: {self.selected_team_name}")
            self.manageTeamWindow.configure(bg="black")
            self.manageTeamWindow.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/edit.png')
            
            self.team_name_label = tk.Label(self.manageTeamWindow, text=f"Team Name: {self.selected_team_name}", font=("Arial", 22))
            self.team_name_label.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
            
            columns = ("Player Name", "Player Credit", "Player Age", "Player No")
            self.player = ttk.Treeview(self.manageTeamWindow, columns=columns, show='headings')
            self.player.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
            column_width = 200
            
            for i, c in enumerate(columns):
                self.player.column(c, width=column_width, anchor=tk.CENTER)
       
            self.player.heading('Player Name', text='Player Name')
            self.player.heading('Player Credit', text='Player Credit')
            self.player.heading('Player Age', text='Player Age')
            self.player.heading('Player No', text='Player No')
        
            player_info = self.controller.get_player_info(self.selected_team_name)
            for info in player_info:
                self.player.insert("", "end", values=(
                    info['Player Name'],
                    info['Player Credit'],
                    info['Player Age'],
                    info['Player No']
                ))
                
            self.player.grid(row=1, column=0, sticky=tk.NSEW)
            
            self.add_button = tk.Button(self.manageTeamWindow, text='Add', command=lambda:self.addPlayer(), bg='black', fg='white')
            self.add_button.grid(row=2, column=0, sticky=tk.NSEW)

            self.update_button = tk.Button(self.manageTeamWindow, text='Update', command=lambda:self.updatePlayer(), state=tk.DISABLED, bg='black', fg='white')
            self.update_button.grid(row=2, column=1, sticky=tk.NSEW)

            self.delete_button = tk.Button(self.manageTeamWindow, text='Delete', command=lambda:self.deletePlayer(), state=tk.DISABLED, bg='black', fg='white')
            self.delete_button.grid(row=2, column=2, sticky=tk.NSEW)

            self.save_and_close_button = tk.Button(self.manageTeamWindow, text='Save and Close', command=self.manageTeamWindow.destroy, bg='black', fg='white')
            self.save_and_close_button.grid(row=2, column=3, sticky=tk.NSEW)
            self.player.bind('<<TreeviewSelect>>', self.on_player_select)
        
    
    def addPlayer(self):
        if self.counterWin <1000:
            self.addPlayer = tk.Toplevel(self)
            self.addPlayer.title("Adding New Player")
            self.addPlayer.configure(bg="black")
            self.addPlayer.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/edit.png')
            
            self.add_player_label = tk.Label(self.addPlayer, text=f"Player Details", font=("Arial", 16))
            self.add_player_label.grid(row=0, column=1, sticky=tk.W, pady=(10, 5))
            
            tk.Label(self.addPlayer, text="Player Name:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, padx=(10, 5))
            player_name_entry = tk.Entry(self.addPlayer, font=("Arial", 12))
            player_name_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
            
            tk.Label(self.addPlayer, text="Player Credit:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.E, padx=(10, 5))
            player_credit_entry = tk.Entry(self.addPlayer, font=("Arial", 12))
            player_credit_entry.grid(row=2, column=1, sticky=tk.W, padx=(0, 10))
            
            tk.Label(self.addPlayer, text="Player Age:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.E, padx=(10, 5))
            player_age_entry = tk.Entry(self.addPlayer, font=("Arial", 12))
            player_age_entry.grid(row=3, column=1, sticky=tk.W, padx=(0, 10))
            
            tk.Label(self.addPlayer, text="Player No:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.E, padx=(10, 5))
            player_no_entry = tk.Entry(self.addPlayer, font=("Arial", 12))
            player_no_entry.grid(row=4, column=1, sticky=tk.W, padx=(0, 10))
            
            self.update_button = tk.Button(self.addPlayer, text='Update', command=self.exit, state=tk.DISABLED, bg='black', fg='white')
            self.update_button.grid(row=5, column=0, sticky=tk.W)
            
            self.add_button = tk.Button(self.addPlayer, text='Add', command=lambda:self.add_new_player_and_update_table(self.selected_team_name,
                player_name_entry.get(), player_credit_entry.get(), player_age_entry.get(),player_no_entry.get()), bg='black', fg='white')
            self.add_button.grid(row=5, column=1, sticky=tk.W)
            
            self.close_button = tk.Button(self.addPlayer, text='Close', command=self.addPlayer.destroy, bg='black', fg='white')
            self.close_button.grid(row=5, column=2, sticky=tk.W)
        else:
            print("reached max limit")
    
    def add_new_player_and_update_table(self, name, player_name, player_credit, player_age, player_no):
        self.controller.add_new_player(name,player_name, player_credit, player_age, player_no)
        player_info = self.controller.get_player_info(self.selected_team_name)
        self.controller.view.update_player_table(player_info)
        self.controller.view.addPlayer.destroy()
        
        
    def on_player_select(self, event):
        selected_item = self.player.selection()
        if selected_item:
            selected_player_info = self.player.item(selected_item, 'values')
            self.selected_player = {
            'Player Name': selected_player_info[0],
            'Player Credit': selected_player_info[1],
            'Player Age': selected_player_info[2],
            'Player No': selected_player_info[3]
        } if selected_player_info else None
            self.update_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.update_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.selected_player = None
        
    def updatePlayer(self):
        if self.counterWin < 1000 and self.selected_player:
            self.counterWin += 1
            self.updatePlayerWindow = tk.Toplevel(self)
            self.updatePlayerWindow.title(f"Updating Player: {self.selected_player['Player Name']}")
            self.updatePlayerWindow.configure(bg="black")
            self.updatePlayerWindow.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/edit.png')
            
            self.add_player_label = tk.Label(self.updatePlayerWindow, text=f"Player Details", font=("Arial", 16))
            self.add_player_label.grid(row=0, column=1, sticky=tk.W, pady=(10, 5))
            
            tk.Label(self.updatePlayerWindow, text="Player Name:", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.E, padx=(10, 5))
            self.player_name_entry = tk.Entry(self.updatePlayerWindow, font=("Arial", 12))
            self.player_name_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 10))
            self.player_name_entry.insert(0, self.selected_player['Player Name'])
            
            tk.Label(self.updatePlayerWindow, text="Player Credit:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.E, padx=(10, 5))
            self.player_credit_entry = tk.Entry(self.updatePlayerWindow, font=("Arial", 12))
            self.player_credit_entry.grid(row=2, column=1, sticky=tk.W, padx=(0, 10))
            self.player_credit_entry.insert(0, self.selected_player['Player Credit'])
            
            tk.Label(self.updatePlayerWindow, text="Player Age:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.E, padx=(10, 5))
            self.player_age_entry = tk.Entry(self.updatePlayerWindow, font=("Arial", 12))
            self.player_age_entry.grid(row=3, column=1, sticky=tk.W, padx=(0, 10))
            self.player_age_entry.insert(0, self.selected_player['Player Age'])
            
            tk.Label(self.updatePlayerWindow, text="Player No:", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.E, padx=(10, 5))
            self.player_no_entry = tk.Entry(self.updatePlayerWindow, font=("Arial", 12))
            self.player_no_entry.grid(row=4, column=1, sticky=tk.W, padx=(0, 10))
            self.player_no_entry.insert(0, self.selected_player['Player No'])
            
            self.update_button = tk.Button(self.updatePlayerWindow, text='Update', command=self.updatePlayer_view_table, bg='black', fg='white')
            self.update_button.grid(row=5, column=0, sticky=tk.W)
            
            self.add_button = tk.Button(self.updatePlayerWindow, text='Add', command=self.exit, state=tk.DISABLED, bg='black', fg='white')
            self.add_button.grid(row=5, column=1, sticky=tk.W)
            
            self.close_button = tk.Button(self.updatePlayerWindow, text='Close', command=self.updatePlayerWindow.destroy, bg='black', fg='white')
            self.close_button.grid(row=5, column=2, sticky=tk.W)
        else:
            print("reached max limit")
           
    def updatePlayer_view_table(self):
        team_name = self.selected_team_name 
        old_player_name = self.selected_player['Player Name']

        new_player_name = self.player_name_entry.get()
        new_player_credit = int(self.player_credit_entry.get())
        new_player_age = int(self.player_age_entry.get())
        new_player_no = int(self.player_no_entry.get())
        
        self.controller.update_player(team_name, old_player_name, new_player_name, new_player_credit, new_player_age, new_player_no)
        
        player_info = self.controller.get_player_info(self.selected_team_name)
        self.update_player_table(player_info)
    
    def update_player_table(self, player_info):
        for i in self.playerTable.get_children():
            self.playerTable.delete(i)
        for info in player_info:
            self.playerTable.insert("", "end", values=(
                info['Player Name'],
                info['Player Credit'],
                info['Player Age'],
                info['Player No']
            ))
        
    def deletePlayer(self):
       selected_item = self.player.selection()
       if selected_item:
            player_name = self.player.item(selected_item)['values'][0]
            team_name = self.selected_team_name
            self.controller.deletePlayer(team_name, player_name)
            
   
    def arrangeSeason(self):
        if self.counterWin < 1000: 
            self.arrangeseason = tk.Toplevel(self)
            self.arrangeseason.title("Arrange a new season")
            self.arrangeseason.configure(bg="black")
            self.arrangeseason.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            image2 = Image.open("/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/NBA_Back.jpg")
            photo2 = ImageTk.PhotoImage(image2)
            label = tk.Label(self.arrangeseason, image=photo2)
            label.image2 = photo2  
            label.grid(row=0, column=0, columnspan=3, sticky=tk.EW)
            
            self.round_button = tk.Button(self.arrangeseason, text = 'Round', command=lambda:self.round(),bg='black', fg='white')
            self.round_button.grid(row=1,column=1, sticky=tk.NSEW)
            
            self.gap_label = tk.Label(self.arrangeseason, bg='black')
            self.gap_label.grid(row=2, column=1)
            
            self.current_button = tk.Button(self.arrangeseason, text = 'Current', command=lambda:self.current(),bg='black', fg='white')
            self.current_button.grid(row=3,column=1, sticky=tk.NSEW)
            
            self.gap_label = tk.Label(self.arrangeseason, bg='black')
            self.gap_label.grid(row=4, column=1)
            
            self.game_button = tk.Button(self.arrangeseason, text = 'Game', command=lambda:self.game(),bg='black', fg='white')
            self.game_button.grid(row=5,column=1, sticky=tk.NSEW)
            
            self.gap_label = tk.Label(self.arrangeseason, bg='black')
            self.gap_label.grid(row=6, column=1)
            
            self.result_button = tk.Button(self.arrangeseason, text = 'Result', command=lambda:self.result(),bg='black', fg='white')
            self.result_button.grid(row=7,column=1, sticky=tk.NSEW)
            
            self.gap_label = tk.Label(self.arrangeseason, bg='black')
            self.gap_label.grid(row=8, column=1)
            
            self.close_button = tk.Button(self.arrangeseason, text='Close', command=self.arrangeseason.destroy, bg='black', fg='white')
            self.close_button.grid(row=9, column=1, sticky=tk.NSEW)
            
        else:
            print("reached max limit")
    
    def round(self):
        if self.counterWin < 1000: 
            self.round_window = tk.Toplevel(self)
            self.round_window.title("Season Rounds")
            self.round_window.configure(bg="black")
            self.round_window.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            self.round_label = tk.Label(self.round_window, text=f"Round: {self.round_number1}", font=("Arial", 16), bg="black", fg="white")
            self.round_label.grid(row=0, column=0, columnspan=3, pady=10)

            self.team_list = tk.Listbox(self.round_window, selectmode=tk.MULTIPLE)
            for team in ["Suns", "Bulls", "Hawks", "Nets"]:
                self.team_list.insert(tk.END, team)
            self.team_list.grid(row=1, column=0, padx=10, pady=10)

            self.game_table = ttk.Treeview(self.round_window, columns=("Team-1", "Team-2"))
            self.game_table.heading("#0", text="Game")
            self.game_table.heading("#1", text="Team-1")
            self.game_table.heading("#2", text="Team-2")
            self.game_table.grid(row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)
            
            self.no_teams_label = tk.Label(self.round_window, text="No teams added to the round", font=("Arial", 14), bg="black", fg="white")
            self.no_teams_label.grid(row=1, column=2, padx=20, pady=10)
            self.no_teams_label.grid_remove()

            self.add_button = tk.Button(self.round_window, text=">>>", command=lambda:self.add_teams_to_game(), bg='black', fg='white')
            self.add_button.grid(row=1, column=1, pady=10)

            self.arrange_button = tk.Button(self.round_window, text="Arrange Season", command=lambda:self.arrangeSeason(), bg='black', fg='white')
            self.arrange_button.grid(row=2, column=1, pady=10)

            self.add_button.config(state=tk.DISABLED)
            self.arrange_button.config(state=tk.DISABLED)
            
            self.team_list.bind("<<ListboxSelect>>", self.update_button_state)
            self.first_round_completed = True
            self.second_round_button.config(state=tk.NORMAL)
            
    def add_teams_to_game(self):
        selected_teams = self.team_list.curselection()
        if len(selected_teams) == 2:
            team1_index, team2_index = selected_teams
            team1 = self.team_list.get(team1_index)
            team2 = self.team_list.get(team2_index)
            self.game_table.insert("", tk.END, text=f"{self.round_number}", values=(team1, team2))
            self.rounds.append((team1, team2))
            
            self.team_list.delete(team2_index)
            self.team_list.delete(team1_index if team1_index < team2_index else team1_index + 1)
            
            
            if self.team_list.size() == 0:
                self.no_teams_label.grid(row=1, column=0, padx=1, pady=10) 
            else:
                self.no_teams_label.grid_remove()
            
            self.round_number += 1
            self.round_label.config(text=f"Round: {self.round_number1}")
            
            if self.round_number == 3:
                self.arrange_button.config(state=tk.NORMAL)
            
            if self.round_number > 2:
                self.round_number = 1
    
    def current(self):
        if self.counterWin < 1000: 
            self.current_window = tk.Toplevel(self)
            self.current_window.title("Tournament")
            self.current_window.configure(bg="black")
            self.current_window.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            self.round_label = tk.Label(self.current_window, text=f"Round: {self.round_number} ", font=("Arial", 16), bg="black", fg="white")
            self.round_label.grid(row=0, column=0, columnspan=4, pady=10)
            
            teams_table = ttk.Treeview(self.current_window, columns=("Teams", " ", "Teams"), show="headings")
            teams_table.heading("#1", text="Teams")
            teams_table.heading("#2", text=" ")
            teams_table.heading("#3", text="Teams")
            teams_table.grid(row=1, column=0, sticky="nsew")

            for round_num, teams_pair in enumerate(self.rounds, start=1):
                teams_table.insert("", tk.END, values=(teams_pair[0], "VS", teams_pair[1]))

            close_button = tk.Button(self.current_window, text="Close", command=self.current_window.destroy, bg='black', fg='white')
            close_button.grid(row=2, column=0, pady=10)

            self.current_window.rowconfigure(1, weight=1)
            self.current_window.columnconfigure(0, weight=1)
    
    def game(self):
        if self.counterWin < 1000:
            self.game_window = tk.Toplevel(self)
            self.game_window.title("All Games Played!")
            self.game_window.configure(bg="black")
            self.game_window.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')

            subheading_label = tk.Label(self.game_window, text="Message:", font=("Arial", 23), bg="black", fg="white")
            subheading_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.NSEW)
            
            if len(self.rounds) == 0:
                message_label = tk.Label(self.game_window, text="No Games to play! Please add games to this round.", bg="black", fg="yellow")
                message_label.grid(row=1, column=0, pady=20)

            elif self.round_number == 3: 
                message = "All games finished! You can check results now! This season ends! Suns is the Champion!!"
                message_label = tk.Label(self.game_window, text=message, bg="black", fg="white")
                message_label.grid(row=1, column=0, pady=20)
                

            elif self.round_number == 1:
                message = "All games finished! You can check results now!"
                message_label = tk.Label(self.game_window, text=message, bg="black", fg="yellow")
                message_label.grid(row=1, column=0, pady=20)

            else:
                pass
            okay_button = tk.Button(self.game_window, text="Okay", command=self.game_window.destroy, bg="black", fg="white")
            okay_button.grid(row=2, column=0, pady=10)

    
    def result(self):
         if self.counterWin < 1000:
            self.result_window = tk.Toplevel(self)
            self.result_window.title("Season Record")
            self.result_window.configure(bg="black")
            self.result_window.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
            
            subheading_label = tk.Label(self.result_window, text="Season Record", font=("Arial", 23), bg="black", fg="white")
            subheading_label.grid(row=0, column=0,columnspan=4, padx=10, pady=5, sticky=tk.NSEW)
            
            self.result_table = ttk.Treeview(self.round_window, columns=("Round", "Game", "Winning Team", "Losing Team"))
            self.result_table.heading("#0", text="Round")
            self.result_table.heading("#1", text="Game")
            self.result_table.heading("#2", text="Winning Team")
            self.result_table.heading("#3", text="Losing Team")
            self.result_table.grid(row=1, column=2, padx=10, pady=10, sticky=tk.NSEW)
            
            results = self.controller.get_round_results()
            for round_num, game_results in enumerate(results, start=1):
                game_num = 1
                for winner, loser in game_results:
                    self.result_table.insert("", tk.END, values=(f"Round {round_num}", f"Game {game_num}", winner, loser))
                    game_num += 1
        
    def exit(self):
        self.destroy()
    
    def set_controller(self, controller):
        self.controller = controller
        teams_info = self.controller.get_team_info()
        allPlayer_info = self.controller.get_allPlayer_info()
        
        if self.selected_team_name:  
            player_info = self.controller.get_player_info(self.selected_team_name)
        else:
            player_info = []
        
        if self.selected_player:
            player_info = self.controller.get_player_info(self.selected_player)
        else:
            player_info=[]
        
    def show_error_message(self, message):
        if self.counterWin < 1000: 
            error_window = tk.Toplevel(self)
            error_window.title("Error!")
            error_window.configure(bg="black")
            error_window.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/error.png')
            
            subheading_label = tk.Label(error_window, text="Message:", bg="black", fg="white")
            subheading_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

            error_label = tk.Label(error_window, text=message, bg="black", fg="yellow")
            error_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

            okay_button = tk.Button(error_window, text='Okay', command=error_window.destroy)
            okay_button.grid(row=2, column=0, padx=10, pady=5, sticky=tk.NSEW)
            
        else:
            print("reached max limit")
    
    def show_error_message1(self, message):
        if self.counterWin < 1000: 
            show_error_message1 = tk.Toplevel(self)
            show_error_message1.title("Input Errors")
            show_error_message1.configure(bg="black")
            show_error_message1.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/error.png')
            
            subheading_label = tk.Label(show_error_message1, text="Message:", bg="black", fg="white")
            subheading_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

            error_label = tk.Label(show_error_message1, text=message, bg="black", fg="yellow")
            error_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

            okay_button = tk.Button(show_error_message1, text='Okay', command=show_error_message1.destroy)
            okay_button.grid(row=2, column=0, padx=10, pady=5, sticky=tk.NSEW)
            
        else:
            print("reached max limit")
            
    def update_team_table(self, teams_info):
        for row in self.treeview.get_children():
            self.treeview.delete(row)
            
        for info in teams_info:
            self.treeview.insert("", "end", values=(
                info['Team Name'],
                info['Number of Players'],
                info['Average Player Credit'],
                info['Average Age']
            )) 
            
    def update_player_table(self, player_info):
        for item in self.player.get_children():
            self.player.delete(item)

        for info in player_info:
            self.player.insert("", "end", values=(
                info['Player Name'],
                info['Player Credit'],
                info['Player Age'],
                info['Player No']
            ))

    def display_player_info(self,allPlayer_info):
        for item in self.allPlayer.get_children():
            self.allPlayer.delete(item)
            
        for info in allPlayer_info:
            self.allPlayer.insert("", "end", values=(
                info['Team'],
                info['Player Name'],
                info['Player Credit'],
                info['Player Age'],
                info['Player No'],
                info ['Player Level']
            ))
            
    def update_players_window(self,filtered_players):
        for row in self.allPlayer.get_children():
            self.allPlayer.delete(row)

        for player_info in filtered_players:
            self.allPlayer.insert("", "end", values=(
                player_info['Team'],
                player_info['Player Name'],
                player_info['Player Credit'],
                player_info['Player Age'],
                player_info['Player No'],
                player_info['Player Level']
            ))
        
        if not filtered_players:
            no_players_label = tk.Label(self, text="Players list is not loaded", font=("Arial", 12), bg="black", fg="white")
            no_players_label.grid(row=2, column=0, columnspan=6, sticky=tk.NSEW)
        
    def on_tree_select(self, event):
        item = self.treeview.selection()
        if item: 
            self.manage_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
            
            selected_item = self.treeview.item(item, 'values')
            self.selected_team_name = selected_item[0] if selected_item else None
        else:
            self.manage_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.selected_team_name = None
    
    def on_player_selected(self, event):
        selected_item = self.treeview.selection()
        
        if selected_item:
            self.update_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
            self.save_and_close_button.config(state=tk.NORMAL)
            self.add_button.config(state=tk.DISABLED)
        else:
            self.update_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)
            self.save_and_close_button.config(state=tk.DISABLED)
            self.add_button.config(state=tk.NORMAL)
    
    def apply_filters(self, event=None):
        level_filter = self.level_filter_entry.get()
        name_filter = self.name_filter_entry.get()
        age_filter_from = self.age_filter_entry_from.get()
        age_filter_to = self.age_filter_entry_to.get()
        
        filtered_info = self.controller.filter_players(level_filter, name_filter, age_filter_from, age_filter_to)

        for row in self.allPlayer.get_children():
            self.allPlayer.delete(row)

        for info in filtered_info:
            self.allPlayer.insert("", "end", values=(
                info['Team'],
                info['Player Name'],
                info['Player Credit'],
                info['Player Age'],
                info['Player No'],
                info['Player Level']
            ))
    
    def update_view_players_label(self, text):
        self.viewPlayersLabel.config(text=text)
    
    def update_button_state(self, event):
        selected_teams = self.team_list.curselection()
        if len(selected_teams) == 2:
            self.add_button.config(state=tk.NORMAL)
        else:
            self.add_button.config(state=tk.DISABLED)