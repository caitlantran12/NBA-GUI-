from Teams import Teams
from Season import Session
import tkinter as tk
from model import Model
from view import View
from controller import Controller

class Association(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.teams = Teams()
        self.session = Session()
        self.title('NBAfx View')
        self.iconbitmap('/Users/caitlantran/Downloads/NBAfx_Python_Scaffold/nba.png')
    
        
        model = Model()
        view = View(self)
        controller = Controller(model, view)
        view.set_controller(controller)
        view.grid(row=0, column=0)


if __name__ == '__main__':
    app = Association()
    app.mainloop()
