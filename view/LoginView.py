import tkinter
from tkinter import *
from tkinter import messagebox
from model.User import User
from service.UserService import UserService
# from view.MainView import App
from view.SelectClassView import SelectClassView

class LoginView:

    def __init__(self):
        self.login_screen = Tk()
        self.username_login_entry =  Entry(self.login_screen)
        self.password__login_entry = Entry(self.login_screen)
        self.username = StringVar(self.username_login_entry, value="teacher")
        self.password = StringVar(self.password__login_entry, value="123456")
        self.token=""

    
    def __processLogin(self,event):
        # messagebox.showinfo('Message', 'Please insert into hopeful')
        username = self.username_login_entry.get()
        password = self.password__login_entry.get()
        user=User(username,password)
        userService = UserService()
        result=userService.getTokenString(user)
        if (result == 0):
            messagebox.showinfo('Error', 'Username or password is incorrect!')
        self.token=result
        self.login_screen.destroy()
        # App(self.token,username,tkinter.Tk(), "Attendance System App")
        select = SelectClassView(self.token, username)
        select.showSelectClassView()

    def showLoginGUI(self):
        self.login_screen.title("Login") #set title for frame
        self.login_screen.geometry("300x250") #set size
        self.login_screen.eval('tk::PlaceWindow . center') #center  
        Label(self.login_screen, text="Please enter login details").pack() #Create label description
        Label(self.login_screen, text="").pack() #Create label with null
        Label(self.login_screen, text="Username").pack() #Create label username
        self.username_login_entry =  Entry(self.login_screen)
        self.password__login_entry = Entry(self.login_screen)
        self.username_login_entry = Entry(self.login_screen, textvariable=self.username)
        self.username_login_entry.pack()
        print(self.username_login_entry.get())
        Label(self.login_screen, text="").pack() #Create label null
        Label(self.login_screen, text="Password").pack() #Create label password
        self.password__login_entry = Entry(self.login_screen, textvariable=self.password, show= '*')
        self.password__login_entry.pack()
        Label(self.login_screen, text="").pack() #Create label null
        btt=Button(self.login_screen, text="Login", width=10, height=1) #Create button
        btt.bind("<Button-1>", self.__processLogin)
        btt.pack()
        self.login_screen.mainloop()