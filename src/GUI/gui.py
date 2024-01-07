# CrossTask Team
# Developer: @zlElo
# Licensed under MIT
# Libarys: CTkListbox, Customtkinter, Psutil


import customtkinter
import psutil
from CTkListbox import *
import threading


def main_gui():
    # Funktion für die Suche
    def search():
        # Suchbegriff aus der Eingabebox abrufen
        query = entry.get()
        # Prozesse in der Liste durchsuchen
        for i in range(process_listbox.size()):
            if query.lower() in process_listbox.get(i).lower():
                pass
            else:
                process_listbox.delete(i)


    def show_process_info():
        # Den ausgewählten Prozess aus der Liste abrufen
        selected_process = process_listbox.get(process_listbox.curselection())
        # Prozessinformationen abrufen
        process = psutil.Process(int(selected_process.split()[0]))
        # CPU und RAM Nutzung des Prozesses abrufen
        cpu_usage = process.cpu_percent(interval=0.5)
        ram_usage = process.memory_percent()
        # Informationen in einem Dialogfeld anzeigen (z.B. mit messageox aus dem tkinter-Modul)
        print("Prozessinformationen", f"CPU-Nutzung: {cpu_usage}%\nRAM-Nutzung: {round(ram_usage, 2)}%")


    def update():
        # CPU
        cpu_perc = psutil.cpu_percent()
        cpu_label.configure(text=f'CPU usage: {cpu_perc}%')
        cpu_progressbar.set(cpu_perc/100)

        # RAM
        ram_perc = psutil.virtual_memory().percent
        ram_label.configure(text=f'RAM usage: {ram_perc}%')
        ram_progressbar.set(ram_perc/100)

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
    root.iconbitmap('src/themes/logo_crosstask.ico')


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


    # Inputbox
    entry = customtkinter.CTkEntry(tabview.tab("Processes"))
    entry.pack(pady=10)


    # Suchbutton erstellen
    search_button = customtkinter.CTkButton(tabview.tab("Processes"), text="Suchen", command=search)
    search_button.pack(pady=10)


    # Task list
    # Create a listbox to display the processes
    process_listbox = CTkListbox(tabview.tab("Processes"))
    process_listbox.pack(pady=10)


    # threading
    process_list_thread = threading.Thread(target=lambda: update_tasklist())
    process_list_thread.start()
    print('[log] started a thread for process list update')

    

    # Button zum Anzeigen der Prozessinformationen erstellen
    show_info_button = customtkinter.CTkButton(tabview.tab("Processes"), text="Prozess-Info abrufen", command=show_process_info)
    show_info_button.pack(pady=10)


    # update loop
    update()

    # root mainloop
    root.mainloop()