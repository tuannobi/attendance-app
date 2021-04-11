import tkinter as tk
from tkinter import ttk
from service.ClassService import ClassService
from view.MainView import App

class SelectClassView:

    def __init__(self, token, username):
        self.window = tk.Tk()
        self.selectedClass = tk.StringVar()
        self.token=token
        self.username=username
        self.classService = ClassService()
        self.classList=self.classService.getClassByTeacherUsername(self.token,self.username)

    def _processChooseClass(self):
        # label.configure(text = "You Have Choosed " + selectedClass.get())
        print(self.selectedClass.get())
        self.window.destroy()
        App(self.token, self.selectedClass.get(), tk.Tk(),"Attedance App")

    def showSelectClassView(self):
        self.window.minsize(600, 400)
        self.window.title("Class Option")
        # self.window.wm_iconbitmap('icon.ico')
        
        label = ttk.Label(self.window, text = "Choose the class: ")
        label.grid(column = 0, row = 0)
        
        
        combobox = ttk.Combobox(self.window, width = 15 , textvariable = self.selectedClass)
        combobox['values'] = self.classList
        combobox.grid(column = 1, row = 0)
        
        button = ttk.Button(self.window, text = "Attend", command = self._processChooseClass)
        button.grid(column = 1, row = 1)
        self.window.mainloop()