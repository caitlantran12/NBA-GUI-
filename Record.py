class Record:
    def __init__(self, win, lose, no, round_num):
        self.WinTeam = win
        self.LoseTeam = lose
        self.GameNumber = no + 1
        self.Round = round_num
