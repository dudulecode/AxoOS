# ------------------------------------------------------------------
#
#       © 2026 Axo. All rights reserved.
#       Reproduction and distribution of AxoOS without written permission from Axo is prohibited.
#
# ------------------------------------------------------------------

from .axomessagebox import AxoMessageBox
from .axoloadingscreen import AxoLoadingScreen

import customtkinter
import os
import pyglet
import sys
import ctypes
import requests
import json

path_ = os.path.dirname(os.path.realpath(__file__))
pyglet.font.add_file(f'System/Fonts/Poppins-Regular.ttf')

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