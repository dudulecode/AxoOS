# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoOS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

import customtkinter
import os
import pyglet
import sys
import ctypes
import requests
import json

path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'System/Fonts/Poppins-Regular.ttf')

def AxoMessageBox(title, text, icon, font_size, *font_style):
    mb = customtkinter.CTk()
    mb.title(title)
    mb.iconbitmap(f'{path_}/{icon}.ico')

    text_ = customtkinter.CTkLabel(mb, text=text, font=("Poppins", font_size, font_style))
    text_.place(relx=0.5, rely=0.45, anchor="center")

    mb.after(0, lambda:mb.state('zoomed'))
    mb.mainloop()