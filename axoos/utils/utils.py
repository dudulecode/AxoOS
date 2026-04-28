import customtkinter
import os
import pyglet
import sys
import ctypes
import requests
import json

path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'{path_}/fonts/Poppins-Regular.ttf')

def AxoMessageBox(title, text, icon, font_size, *font_style):
    mb = customtkinter.CTk()
    mb.title(title)
    mb.geometry("400x200")
    mb.iconbitmap(f'{path_}/{icon}.ico')

    text_ = customtkinter.CTkLabel(mb, text=text, font=("Poppins", font_size, font_style)).place(x=200, y=100, anchor=customtkinter.CENTER)

    mb.minsize(width=400, height=200)
    mb.maxsize(width=400, height=200)
    mb.mainloop()

def AxoLoadingScreen(text, timeout):
    loading = customtkinter.CTk()
    loading.title("AxoOS")
    # loading.geometry("1600x1200")
    loading.iconbitmap(f'{path_}/resources/blue.ico')

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

def AxoUpdate():
    AxoLoadingScreen("Checking for updates...", 3000)
    headers = {'Accept': 'application/json'}
    r = requests.get('https://raw.githubusercontent.com/dudulecode/AxoOS/refs/heads/main/update.json', headers=headers)
    r_json = r.json()
    r_str = json.dumps(r_json)
    r_resp = json.loads(r_str)
    with open(f"C:/Users/{os.getlogin()}/AxoOS/User Data/version.axo") as file:
        current_version = file.read()
        if current_version == r_resp['current_version']:
            pass
        else:
            AxoMessageBox("AxoOS", f"New version available:\n{current_version} -> {r_resp['current_version']}\nTo install the new update, go on\nthe AxoOS github repository\nand download the latest release.", "warning", 20, "bold")
    # AxoMessageBox("AxoOS", f"Current version: {r_resp['current_version']}", "information", 10)
