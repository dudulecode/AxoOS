# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoIS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

from utils import utils

import customtkinter
import os
import pyglet
import subprocess
import json
import requests
import sys
import ctypes

path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'{path_}/fonts/Poppins-Regular.ttf')

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
    utils.AxoMessageBox("AxoOS", "Seems like it's the first time you're using AxoOS...\nwelcome on AxoOS!\nAxoOS is a \"fake\" operating system\nwritten fully in Python (only availabe on Windows 10/11)", "information", 18)
except FileExistsError:
    pass

utils.AxoLoadingScreen("Loading...", 2000)
utils.AxoUpdate()