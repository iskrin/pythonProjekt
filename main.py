import login as log
import gui
import readme as r
import tkinter as tk
import os

fileName = "users.txt"
window = tk.Tk()
frame = tk.Frame(window)
frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky='ew')
window.grid_columnconfigure(0,weight=1)

usersList = tk.Listbox(frame, height=10, width=50, selectmode="SINGLE")
loginButton = tk.Button(frame, text="Zaloguj", width=35, command=lambda: login(frame, window, usersList, fileName))


def login(frame, window, tasksList, fileName):
    currentSelection = tasksList.curselection()
    username = tasksList.get(currentSelection[0]).strip()
    r.save(tasksList, fileName)

    for widget in frame.winfo_children():
        widget.destroy()

    window.geometry("493x420")
    window.configure(bg = "#FFFFFF")
    r.currentUser = username

    parentDir = os.getcwd() 
    pathToCreate = "users\\" + username
    r.userPath = os.path.join(parentDir, pathToCreate)

    r.loadFavouritesList(r.currentUser, r.userPath, r.favouritesList)
    gui.startPokemon(window)
    


def saveAndExit(window, tasksList, fileName):
    r.save(tasksList, fileName)
    window.destroy()
   

window.protocol("WM_DELETE_WINDOW",lambda: saveAndExit(window, usersList, r.fileName))
log.startLogin(window, frame, usersList, loginButton)