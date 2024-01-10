# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import customtkinter


def about_developer_win():
    root = customtkinter.CTk()
    root.geometry('360x120')
    root.title('Developers')

    # label
    label = customtkinter.CTkLabel(root, text='Coded under the GPL v3.0 License by following developers:').pack(pady=10)

    # developer frame
    frame = customtkinter.CTkFrame(root)
    frame.pack()

    # developers
    developer1 = customtkinter.CTkLabel(frame, text='- @DarkGloves').pack(padx=60)
    developer2 = customtkinter.CTkLabel(frame, text='- @zlElo').pack()

    root.mainloop()