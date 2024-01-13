# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from customtkinter import *
import customtkinter
import json
import platform
import os


class SettingsWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('350x250')
        self.resizable(False, False)
        self.title('Settings')

        # read settings
        with open('config/settings.json', 'r') as f:
            data = json.load(f)
            _version = data['theme']
        f.close()

        self.frame = CTkFrame(self)
        self.frame.pack(pady=10)

        # theme selection
        combobox_var = customtkinter.StringVar(value=_version)
        CTkLabel(self.frame, text='Theme:').pack()
        self.theme_selection_ = CTkComboBox(self.frame, values=["System", "Dark", "White"], variable=combobox_var)
        self.theme_selection_.pack()

        # platform check for window icon
        operating_system = platform.system()
        if  operating_system == 'Windows':
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))
        elif operating_system == 'Linux':
            pass
        else:
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))