# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter
from PIL import Image


def about_program_win():
    root = customtkinter.CTk()
    root.geometry('350x200')
    root.title('About')

    img = customtkinter.CTkImage(light_image=Image.open('content/logo_crosstask-removebg.png'), dark_image=Image.open('content/logo_crosstask-removebg.png'), size=(200, 200))
    label = customtkinter.CTkLabel(root, image=img, text='')
    label.grid(column=0, row=0)

    # infos
    program_info = customtkinter.CTkLabel(root, text='CrossTask\n\nVersion: v1.02-beta')
    program_info.grid(column=4, row=0)


    root.mainloop()

