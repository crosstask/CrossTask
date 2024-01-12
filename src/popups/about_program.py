# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter
from customtkinter import CTkToplevel
from PIL import Image
import json


class AboutPopup(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('350x215')
        self.resizable(False, False)
        self.title('About')
        self.img = customtkinter.CTkImage(light_image=Image.open('content/logo_crosstask-removebg.png'), dark_image=Image.open('content/logo_crosstask-removebg.png'), size=(200, 200))
        self.label = customtkinter.CTkLabel(self, image=self.img, text='')
        self.label.grid(column=0, row=0)

        # read settings
        with open('config/settings.json', 'r') as f:
            data = json.load(f)
            _version = data['version']
        f.close()

        # infos
        self.program_info = customtkinter.CTkLabel(self, text=f'CrossTask\n\nVersion: v{_version}')
        self.program_info.grid(column=4, row=0)
