# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from customtkinter import *
import tkinter as tk
import customtkinter
import json
import platform
import os


class SettingsWindow(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('200x150')
        self.resizable(False, False)
        self.title('Settings')

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

        # platform check for window icon
        operating_system = platform.system()
        if  operating_system == 'Windows':
            self.after(200, lambda: self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico')))
        elif operating_system == 'Linux':
            pass
        else:
            # setup macos window icon
            img = tk.Image("photo", file="content/logo_crosstask-removebg.png")
            self.after(200, lambda: self.tk.call('wm','iconphoto', self._w, img))

        self._settings()

    def _settings(self):
        # read settings
        doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
        with open(f'{doc_path}/CrossTask/Settings/settings.json', 'r') as f:
            data = json.load(f)
            theme = data['theme']
        f.close()

        # settings
        self.frame = CTkFrame(self)
        self.frame.pack(pady=10)

        # theme selection
        combobox_var = customtkinter.StringVar(value=theme)
        label = CTkLabel(self.frame, text='Theme:').pack()
        self.theme_selection_ = CTkComboBox(self.frame, values=["System", "Dark", "White"], variable=combobox_var)
        self.theme_selection_.pack(padx=10)

        self.button_save_theme = CTkButton(self.frame, text='Save', command=lambda: self.__save_settings_theme(self.theme_selection_))
        self.button_save_theme.pack(pady=7)

    def __save_settings_theme(self, box):
        # read settings
        doc_path = os.path.join(os.path.expanduser('~'), 'Documents')
        with open(f'{doc_path}/CrossTask/Settings/settings.json', 'r') as file:
            data = json.load(file)
            data['theme'] = box.get()

        with open(f'{doc_path}/CrossTask/Settings/settings.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        theme_id = data['theme']
        print(theme_id)

        # update ui
        customtkinter.set_appearance_mode(theme_id)