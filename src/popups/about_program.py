# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter
from customtkinter import CTkToplevel
from PIL import Image
import json
import platform
import os


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

        # platform check for window icon
        operating_system = platform.system()
        if  operating_system == 'Windows':
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))
        elif operating_system == 'Linux':
            pass
        else:
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))
