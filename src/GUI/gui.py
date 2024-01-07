# CrossTask Team
# Developer: @zlElo
# Licensed under MIT
# Libarys: CTkListbox, Customtkinter, Psutil


import customtkinter
import psutil
from CTkListbox import *
import threading


def main_gui():
    def update():
        # CPU
        cpu_label.configure(text=f'CPU usage: {psutil.cpu_percent()}%')
        cpu_progressbar.set(psutil.cpu_percent()/100)

        # RAM
        ram_label.configure(text=f'RAM usage: {psutil.virtual_memory().percent}%')
        ram_progressbar.set(psutil.virtual_memory().percent/100)

        # DISK
        disk_label.configure(text=f'Disk usage: {psutil.disk_usage("/").percent}%')
        disk_progressbar.set(psutil.disk_usage("/").percent/100)

        root.after(1000, update)


    def update_tasklist():
        # info
        reload_label = customtkinter.CTkLabel(tabview.tab("Processes"), text='(Re)load index...')
        reload_label.pack()

        # Task list
        # Get the list of all processes
        processes = psutil.process_iter(['pid', 'name'])
        # Clear the existing listbox
        process_listbox.delete(1, "END")
        # Insert the updated process list into the listbox
        for proc in processes:
            process_listbox.insert("END", f"{proc.info['pid']} - {proc.info['name']}")

        
        reload_label.destroy()
        root.after(30000, update_tasklist)

        

    root = customtkinter.CTk()
    root.geometry('290x400')
    root.title('CrossTask')


    # Create the Tabbed View
    tabview = customtkinter.CTkTabview(root)
    tabview.pack(padx=20, pady=20)

    tabview.add("Overview")  # Overview tab
    tabview.add("Processes")  # Process tab
    tabview.set("Overview")  # set overview as currently visible tab


    # Create Frames
    frame_cpu = customtkinter.CTkFrame(master=tabview.tab("Overview"))
    frame_cpu.pack(pady=25)

    frame_ram = customtkinter.CTkFrame(master=tabview.tab("Overview"))
    frame_ram.pack(pady=25)

    frame_disk = customtkinter.CTkFrame(master=tabview.tab("Overview"))
    frame_disk.pack(pady=25)


    # CPU
    cpu_label = customtkinter.CTkLabel(frame_cpu, text=f'CPU usage: {psutil.cpu_percent()}%')
    cpu_label.pack()

    cpu_progressbar = customtkinter.CTkProgressBar(frame_cpu)
    cpu_progressbar.pack(padx=20)


    # RAM
    ram_label = customtkinter.CTkLabel(frame_ram, text=f'RAM usage: {psutil.virtual_memory().percent}%')
    ram_label.pack()

    ram_progressbar = customtkinter.CTkProgressBar(frame_ram)
    ram_progressbar.pack(padx=20)


    # DISK
    disk_label = customtkinter.CTkLabel(frame_disk, text=f'Disk usage: {psutil.disk_usage("/").percent}%')
    disk_label.pack()

    disk_progressbar = customtkinter.CTkProgressBar(frame_disk)
    disk_progressbar.pack(padx=20)

    
    # Task list
    # Create a listbox to display the processes
    process_listbox = CTkListbox(tabview.tab("Processes"))
    process_listbox.pack(pady=10)


    # threading
    process_list_thread = threading.Thread(target=lambda: update_tasklist())
    process_list_thread.start()
    print('[log] started a thread for process list update')


    # update loop
    update()

    # root mainloop
    root.mainloop()