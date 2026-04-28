# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoOS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

from .axomessagebox import AxoMessageBox

import customtkinter
import os
import pyglet
import sys
import ctypes
import requests
import json

# path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'System/Fonts/Poppins-Regular.ttf')

def AxoSecurityCheck():
    def files_exist(file_list):
        file_found = None
        for item in file_list:
            if not os.path.isfile(item):
                AxoMessageBox("AxoOS", f"Error: AxoOS can't boot because \"{item}\" missing from your computer. Try reinstalling AxoOS to fix this problem.", "error", 25, "bold")
                sys.exit()

    files = [f'C:/Users/{os.getlogin()}/AxoOS/User Data/axo.json', f'C:/Users/{os.getlogin()}/AxoOS/User Data/user.axo', f'C:/Users/{os.getlogin()}/AxoOS/User Data/version.axo']
    files_exist(files)