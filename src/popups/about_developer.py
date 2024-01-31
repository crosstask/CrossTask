# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from customtkinter import *
from PIL import Image
import tkinter as tk
import os
import webbrowser
import platform


class Icons():
    def __init__(self, size:tuple) -> None:
        self.github = CTkImage(Image.open(os.path.join(os.getcwd(), 'img', 'light', 'github.png')), Image.open(os.path.join(os.getcwd(), 'img', 'dark', 'github.png')), size=size)
        self.mail = CTkImage(Image.open(os.path.join(os.getcwd(), 'img', 'light', 'mail.png')), Image.open(os.path.join(os.getcwd(), 'img', 'dark', 'mail.png')), size=size)
        self.telegram = CTkImage(Image.open(os.path.join(os.getcwd(), 'img', 'light', 'telegram.png')), Image.open(os.path.join(os.getcwd(), 'img', 'dark', 'telegram.png')), size=size)

class DevelopersPopup(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry('400x190')
        self.resizable(False, False)
        self.title('Developers')

        CTkLabel(self, text='This project has been developed by:', font=('Arial', 16, 'bold')).pack(pady=10)
        self._developerFrame('DarkGloves', 'https://github.com/DarkGloves').pack(pady=15)
        self._developerFrame('zlElo', 'https://github.com/zlElo').pack(pady=(0,5))

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
        

    def _developerFrame(self, devName:str, githubProfile:str=False, mailAdress:str=False):
        frame = CTkFrame(self, corner_radius=5)
        frame.rowconfigure((0), weight=1)
        frame.columnconfigure((0), weight=8)
        frame.columnconfigure((1,2), weight=1)
        CTkLabel(frame, text=devName, font=('Arial', 16)).grid(row=0, column=0, pady=5, sticky=NSEW, padx=5)
        CTkButton(frame, text=None, hover_color='gray30', image=Icons((20,20)).github, width=0, height=0,fg_color='transparent', corner_radius=15, command=lambda : webbrowser.open(githubProfile)).grid(column=1, row=0, padx=10) if githubProfile else None 
        CTkButton(frame, text=None, hover_color='gray30', image=Icons((20,20)).mail, width=0, height=0,fg_color='transparent', corner_radius=15).grid(column=2, row=0, padx=(0,10)) if mailAdress else None 
        return frame
        