# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter
from customtkinter import CTkToplevel
import json


class SettingsWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('350x250')
        self.resizable(False, False)
        self.title('Settings')

        # read settings
        with open('config/settings.json', 'r') as f:
            data = json.load(f)
            _version = data['autorefresh-state']
        f.close()
