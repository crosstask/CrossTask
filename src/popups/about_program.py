# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter
from customtkinter import CTkToplevel
import tkinter as tk
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

        # read settings
        doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
        with open(f'{doc_path}/CrossTask/Settings/settings.json', 'r') as f:
            data = json.load(f)
            theme = data['theme']
        f.close()
        
        if theme == "System":
            customtkinter.set_appearance_mode("system")
        elif theme == "Dark":
            customtkinter.set_appearance_mode("dark")
        elif theme == "White":
            customtkinter.set_appearance_mode("white")

        self.img = customtkinter.CTkImage(light_image=Image.open('content/logo_crosstask-removebg.png'), dark_image=Image.open('content/logo_crosstask-removebg.png'), size=(200, 200))
        self.label = customtkinter.CTkLabel(self, image=self.img, text='')
        self.label.grid(column=0, row=0)

        # read settings
        with open(f'{doc_path}/CrossTask/Settings/settings.json', 'r') as f:
            data = json.load(f)
            _version = data['version']
        f.close()

        # infos
        self.program_info = customtkinter.CTkLabel(self, text=f'CrossTask\n\nVersion: v{_version}')
        self.program_info.grid(column=4, row=0)

        # platform check for window icon
        operating_system = platform.system()
        print(os.path.join(os.getcwd(), 'img', 'bitmap.ico'))
        if  operating_system == 'Windows':
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))
        elif operating_system == 'Linux':
            pass
        else:
            # setup macos window icon
            img = tk.Image("photo", file="content/logo_crosstask-removebg.png")
            self.after(200, lambda: self.tk.call('wm','iconphoto', self._w, img))
