import projekt as projekt
from pathlib import Path
from tkinter import *
import tkinter as tk
import os
import readme as r


DIRNAME = os.path.dirname(__file__)
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = os.path.join(DIRNAME,"build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def startPokemon(window):
    

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 420,
        width = 493,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))

    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: r.changeName(canvas, image_1, canvasText),
        relief="flat"
    )

    button_1.place(
        x=109.0,
        y=308.0,
        width=275.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))

    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: projekt.savePokemon(r.image_url, str(r.data['name'].capitalize()) + ".png", r.userPath),
        relief="flat"
    )

    button_2.place(
        x=109.0,
        y=357.0,
        width=275.0,
        height=34.0
    )

    canvasText = canvas.create_text(
        int(canvas['width']) / 2,
        int(canvas['height']) / 2,
        anchor= "n",
        text=str(r.data['name'].capitalize()),
        fill="#000000",
        font=("Inter Black", 16)
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: r.saveAsFavourite(r.favouritesList, r.currentUser, r.userPath),
        relief="flat"
    )
    button_3.place(
        x=438.0,
        y=10.0,
        width=43.0,
        height=43.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: r.showFavourites(r.favouritesList),
        relief="flat"
    )
    button_4.place(
        x=370.0,
        y=10.0,
        width=43.0,
        height=43.0
    )

    pokemonImage = projekt.display_image_from_url(r.image_url)
    image_1 = canvas.create_image(
        int(canvas['width']) / 2,
        int(canvas['height']) / 2 - 100,
        image=pokemonImage
    )


    window.resizable(False, False)
    window.mainloop()

