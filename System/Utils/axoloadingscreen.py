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

# path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'System/Fonts/Poppins-Regular.ttf')

def AxoLoadingScreen(text, timeout):
    loading = customtkinter.CTk()
    loading.title("AxoOS")
    # loading.geometry("1600x1200")
    loading.iconbitmap(f'System/Fonts/Poppins-Regular.ttf')

    def finish_animation():
        progress_bar.stop()
        loading.destroy()

    # Loading label
    loading_label = customtkinter.CTkLabel(loading, text=text, font=("Poppins", 40, "bold"))
    loading_label.place(relx=0.5, rely=0.45, anchor="center")

    # Progress bar
    progress_bar = customtkinter.CTkProgressBar(loading, orientation="horizontal", width=500, progress_color="#2039AD")
    progress_bar.configure(mode="indeterminate")
    progress_bar.place(relx=0.5, rely=0.5, anchor="center")

    # Schedule closing the loading window after 5 seconds
    loading.after(timeout, finish_animation)

    # Start the progress bar animation
    progress_bar.start()


    loading.after(0, lambda:loading.state('zoomed'))
    loading.mainloop()