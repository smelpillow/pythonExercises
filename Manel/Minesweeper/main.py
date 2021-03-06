# Instrucciones en este video https://www.youtube.com/watch?v=OqbGRZx4xUc&t=9s

from ctypes import util
from tkinter import *
from unicodedata import name
import settings
import utils
from cell import Cell

root = Tk()
# Datos de config de la ventana
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Buscador de Minas')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25), 
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

print(Cell.all)

# Arranca la ventana
root.mainloop()