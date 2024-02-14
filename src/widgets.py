# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from customtkinter import *
from tkinter import *


class ScrollableListbox(CTkFrame):
    def __init__(self, master, appearance_mode:str='dark', listvariable=None):
        super().__init__(master, corner_radius=199)
        self.List = Listbox(self, listvariable=listvariable)
        self.scrollbar = CTkScrollbar(self, command=self.List.yview)
        self.List.config(yscrollcommand=self.scrollbar.set)
        self._Dark if appearance_mode.lower == 'dark' else self._Light
        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)
        self.List.grid(row=0, column=0, sticky='NSEW')
        self.scrollbar.grid(row=0, column=0, sticky='NSE', padx=2)

    def _Dark(self):
        set_appearance_mode('dark')
        self.List.configure(background='gray20', fg_color = 'FFFFFF', )
    
    def _Light(self):
        set_appearance_mode('light')
        self.List.configure(background='FFFFFF', fg_color = '000000', )


# # Testing:
            
# root = Tk()
# var = StringVar(value=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,])
# list1 = ScrollableListbox(root,listvariable=var)
# list1.pack(fill=BOTH, expand=True)
# CTkButton(root, command=lambda:print(list1.List.get(list1.List.curselection()))).pack()
# root.mainloop()