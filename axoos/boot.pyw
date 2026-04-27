# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoIS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

from utils.axomessagebox import AxoMessageBox

import customtkinter
import os
import sys
import threading
import time
import ctypes

path_ = os.path.dirname(os.path.realpath(__file__))

try:
    os.makedirs(f"C:/Users/{os.getlogin()}/AxoOS/User Data")
    AxoMessageBox("AxoOS", "Seems like it's the first time you're using AxoOS...\nWelcome on AxoOS!\nAxoOS is a \"fake\" operating system written\nfully in Python (only availabe on Windows 10/11)", "information", 17)
except FileExistsError:
    pass

# ---------------- LOADING SCREEN ----------------
class SplashScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.overrideredirect(True)  # remove window borders
        self.geometry("500x300")
        self.configure(fg_color="#1a1a1a")

        # Center window
        x = (self.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.winfo_screenheight() // 2) - (300 // 2)
        self.geometry(f"+{x}+{y}")

        self.label = customtkinter.CTkLabel(
            self,
            text="Starting AxoOS...",
            font=("Arial", 20)
        )
        self.label.pack(pady=40)

        self.progress = customtkinter.CTkProgressBar(self, width=300)
        self.progress.pack(pady=20)
        self.progress.set(0)

        self.status = customtkinter.CTkLabel(
            self,
            text="Loading modules...",
            font=("Arial", 12)
        )
        self.status.pack(pady=10)

        threading.Thread(target=self.load).start()

    def load(self):
        steps = [
            ("Initializing system...", 0.2),
            ("Loading UI...", 0.4),
            ("Preparing environment...", 0.6),
            ("Finalizing...", 0.8),
            ("Done!", 1.0)
        ]

        for text, value in steps:
            time.sleep(0.7)
            self.progress.set(value)
            self.status.configure(text=text)

        time.sleep(0.5)
        self.destroy()
        start_main_app()


# ---------------- MAIN APP ----------------
def start_main_app():
    boot = customtkinter.CTk()
    boot.title("AxoOS")
    boot.iconbitmap(f'{path_}/resources/blue.ico')

    boot.after(0, lambda: boot.state('zoomed'))

    label = customtkinter.CTkLabel(
        boot,
        text="Welcome to AxoOS",
        font=("Arial", 24)
    )
    label.pack(pady=50)

    boot.mainloop()


# ---------------- START ----------------
if __name__ == "__main__":
    splash = SplashScreen()
    splash.mainloop()