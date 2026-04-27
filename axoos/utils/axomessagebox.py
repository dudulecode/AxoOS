# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoIS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

import ctypes
import threading
import customtkinter
import os
import pyglet
import time

path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'{path_}/fonts/Poppins-Regular.ttf')

def AxoMessageBox(title, text, icon, font_size):
    mb = customtkinter.CTk()
    mb.title(title)
    mb.geometry("400x200")
    mb.iconbitmap(f'{path_}/{icon}.ico')

    text_ = customtkinter.CTkLabel(mb, text=text, font=("Poppins", font_size)).place(x=200, y=100, anchor=customtkinter.CENTER)

    mb.minsize(width=400, height=200)
    mb.maxsize(width=400, height=200)
    mb.mainloop()