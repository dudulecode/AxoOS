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
import ctypes

path_ = os.path.dirname(os.path.realpath(__file__))

try:
    os.makedirs(f"C:/Users/{os.getlogin()}/AxoOS/User Data")
    AxoMessageBox("AxoOS", "Seems like it's the first time you're using AxoOS...\nwelcome on AxoOS!\nAxoOS is a \"fake\" operating system\nwritten fully in Python (only availabe on Windows 10/11)", "information")
except FileExistsError:
    pass

boot = customtkinter.CTk()
boot.title("AxoOS")
# boot.geometry("1600x1200")
boot.iconbitmap(f'{path_}/resources/blue.ico')

boot.after(0, lambda:boot.state('zoomed'))
boot.mainloop()