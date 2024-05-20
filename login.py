import tkinter as tk
import projekt
import readme as r


def startLogin(window, frame, tasksList, loginButton):
    #lista tasków
    tasksList.pack(padx=10, pady=10)

    #Kontener na input i przycisk do dodawanie tasków
    inputFrame = tk.Frame(frame)
    inputFrame.pack(pady=5)

    #Input
    tasksInput = tk.Entry(inputFrame, width=30)
    tasksInput.pack(side=tk.LEFT)

    #Przycisk do dodawania taska
    addTaskButton = tk.Button(inputFrame, text="Dodaj użytkownika", command=lambda: r.addUser(tasksList, tasksInput))
    addTaskButton.pack(side=tk.RIGHT, padx=10)

    #Przycisk do logowania
    loginButton.pack()
    r.readUsers(r.fileName, tasksList)
    frame.mainloop()

