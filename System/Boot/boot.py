# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoOS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

import customtkinter
import os
import pyglet
import subprocess
import json
import requests
import sys
import ctypes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from ..Utils.axomessagebox import *
from ..Utils.axoloadingscreen import *
from ..Utils.axosecuritycheck import *
from ..Utils.axoupdate import *

# path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'System/Fonts/Poppins-Regular.ttf')

def run_axo():
    try:
        os.makedirs(f"C:/Users/{os.getlogin()}/AxoOS/User Data")
        try:
            with open(f"C:/Users/{os.getlogin()}/AxoOS/User Data/user.axo", "x") as file:
                file.write("-------- DO NOT TOUCH THIS FILE --------\ndefaultuser0")
        except FileExistsError:
            pass
        try:
            try:
                with open(f"C:/Users/{os.getlogin()}/AxoOS/User Data/version.axo", "x") as file:
                    headers = {'Accept': 'application/json'}
                    r = requests.get('https://raw.githubusercontent.com/dudulecode/AxoOS/refs/heads/main/update.json', headers=headers)
                    r_json = r.json()
                    r_str = json.dumps(r_json)
                    r_resp = json.loads(r_str)
                    file.write(r_resp['current_version'])
            except FileExistsError:
                pass
        except FileExistsError:
            pass
        AxoMessageBox("AxoOS", "Seems like it's the first time you're using AxoOS...\nwelcome on AxoOS!\nAxoOS is a \"fake\" operating system\nwritten fully in Python (only availabe on Windows 10/11)", "information", 18)
    except FileExistsError:
        pass

    AxoLoadingScreen("Loading...", 2000)
    AxoLoadingScreen("Verifying files...", 1000)
    AxoSecurityCheck()
    AxoUpdate()