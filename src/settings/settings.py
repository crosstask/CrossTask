# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from customtkinter import CTkToplevel
import json
import platform
import os


class SettingsWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('350x250')
        self.resizable(False, False)
        self.title('Settings')
        
        # platform check for window icon
        operating_system = platform.system()
        if  operating_system == 'Windows':
            self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico'))
        elif operating_system == 'Linux':
            pass
        else:
            self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico'))

        # read settings
        with open('config/settings.json', 'r') as f:
            data = json.load(f)
            _version = data['autorefresh-state']
        f.close()
