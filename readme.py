import projekt
from random import randrange
from tkinter import messagebox
import tkinter as tk
import os
from collections import Counter


currentPokemonIndex = str(randrange(500) + 1)
image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(currentPokemonIndex) + ".png"
data = projekt.fetch_data_from_api("https://pokeapi.co/api/v2/pokemon/" + str(currentPokemonIndex))
fileName = "users.txt"
currentUser = ""
userPath = ""
favouritesList = []



def changeName(canvas, targetImage, targetText):
    
    global pokemonImage
    global data
    global image_url

    currentPokemonIndex = str(randrange(500) + 1)  
    image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(currentPokemonIndex) + ".png"
    data = projekt.fetch_data_from_api("https://pokeapi.co/api/v2/pokemon/" + str(currentPokemonIndex))
    pokemonImage = projekt.display_image_from_url(image_url) 
    canvas.itemconfig(targetText, text=data['name'].capitalize())
    canvas.itemconfig(targetImage, image=pokemonImage)
    
def loadFavouritesList(username, userpath, favouritesList):
    if os.path.exists(userpath + "\\" + username.strip()+".txt"):
        file = open(userpath + "\\" + username.strip()+".txt", 'r')
        lines = file.readlines()
        for line in lines:
           favouritesList.append(line.strip())
       
   
def saveAsFavourite(favouritesList, username, userpath):
    if(str(data["name"]) in favouritesList):
        messagebox.showwarning("Błąd", "Ten Pokemon jest już na twojej liście ulubionych") 
    else:
        username = str(username.strip())
        favouritesList.append(str(data["name"]))

        if not os.path.exists(userpath):      
            os.mkdir(userpath)

        with open(userpath + "\\" + username + ".txt", "w") as txt_file:
            for element in favouritesList:
                txt_file.write(element + "\n")

def showFavourites(favouritesList):
    favouritesText = ""
    for element in favouritesList:
        favouritesText += str(element.capitalize()  + ", ")
    favouritesText = "Twoje ulubione Pokemony to: " + favouritesText[:-2]
    messagebox.showwarning(title="siema", message=favouritesText, icon=None)
    
def addUser(tasksList, tasksInput):
    taskText = tasksInput.get()
    tasks = tasksList.get(0, tk.END)
    print(tasks)
    if taskText != "" and (taskText + "\n") not in tasks:
        tasksInput.delete(0, tk.END)
        tasksList.insert(tk.END, taskText + "\n")
    else:
        messagebox.showwarning(title="Error", message="Nazwa jest pusta lub zajęta")

def readUsers(filename, usersList):
    tasks = []
    if os.path.exists(filename):
        file = open(filename, 'r')
        tasks = file.readlines()
        for task in tasks:
            usersList.insert(tk.END, task)

def save(tasksList, fileName):
    try:
        content = list(tasksList.get(0, tk.END))
        file = open(fileName, "w")
        file.writelines(content)
        file.close()
    except: 
        return

def clearWindow(window, tasksList, fileName):
    content = list(tasksList.get(0, tk.END))
    print(content)
    file = open(fileName, "w")
    file.writelines(content)
    file.close()
    window.destroy()

def showRanking(directory):
    pokemonCounter = Counter()

    # Przejdź przez wszystkie podfoldery i pliki w folderze users
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        pokemon = line.strip()
                        if pokemon:
                            pokemonCounter[pokemon] += 1
    
    rankingText = ""
    pokemonCounterSorted = dict(sorted(pokemonCounter.items(), key=lambda item: item[1], reverse=True))
    for key, value in pokemonCounterSorted.items():
         rankingText = rankingText + f" {key}:" + f" {value}\n"
    
    messagebox.showwarning(title="Ranking", message= rankingText, icon=None)



