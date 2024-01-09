# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL
# Libarys: CTkListbox, Customtkinter, Psutil <= Do a fucking requierements.txt plz :)

###########
# MODULES #
###########
from customtkinter import *
import psutil
from CTkListbox import *
import os
import threading

# Commented cause of full rewrite ~ DarkGloves

# def main_gui():
#     def search():
#         query = entry.get()
#         for i in range(process_listbox.size()):
#             if query.lower() in process_listbox.get(i).lower():
#                 pass
#             else:
#                 process_listbox.delete(i)


#     def show_process_info():
#         # Den ausgewählten Prozess aus der Liste abrufen
#         selected_process = process_listbox.get(process_listbox.curselection())
#         # Prozessinformationen abrufen
#         process = psutil.Process(int(selected_process.split()[0]))
#         # CPU und RAM Nutzung des Prozesses abrufen
#         cpu_usage = process.cpu_percent(interval=0.5)
#         ram_usage = process.memory_percent()
#         # Informationen in einem Dialogfeld anzeigen (z.B. mit messageox aus dem tkinter-Modul)
#         print("Prozessinformationen", f"CPU-Nutzung: {cpu_usage}%\nRAM-Nutzung: {round(ram_usage, 2)}%")


#     def update():
#         # CPU
#         cpu_perc = psutil.cpu_percent()
#         cpu_label.configure(text=f'CPU usage: {cpu_perc}%')
#         cpu_progressbar.set(cpu_perc/100)

#         # RAM
#         ram_perc = psutil.virtual_memory().percent
#         ram_label.configure(text=f'RAM usage: {ram_perc}%')
#         ram_progressbar.set(ram_perc/100)

#         # DISK
#         disk_label.configure(text=f'Disk usage: {psutil.disk_usage("/").percent}%')
#         disk_progressbar.set(psutil.disk_usage("/").percent/100)

#         root.after(1000, update)


#     def update_tasklist():
#         # info
#         reload_label = CTkLabel(tabview.tab("Processes"), text='(Re)load index...')
#         reload_label.pack()

#         # Task list
#         # Get the list of all processes
#         processes = psutil.process_iter(['pid', 'name'])
#         # Clear the existing listbox
#         process_listbox.delete(1, "END")
#         # Insert the updated process list into the listbox
#         for proc in processes:
#             process_listbox.insert("END", f"{proc.info['pid']} - {proc.info['name']}")

        
#         reload_label.destroy()
#         root.after(30000, update_tasklist)

        

#     root = CTk()
#     root.geometry('290x500')
#     root.title('CrossTask')
#     root.iconbitmap('src/themes/logo_crosstask.ico') # Imagine the program is executed from here by some reason


#     # Create the Tabbed View
#     tabview = CTkTabview(root)
#     tabview.pack(padx=20, pady=20)

#     tabview.add("Overview")  # Overview tab
#     tabview.add("Processes")  # Process tab
#     tabview.set("Overview")  # set overview as currently visible tab


#     # Create Frames
#     frame_cpu = CTkFrame(master=tabview.tab("Overview"))
#     frame_cpu.pack(pady=25)

#     frame_ram = CTkFrame(master=tabview.tab("Overview"))
#     frame_ram.pack(pady=25)

#     frame_disk = CTkFrame(master=tabview.tab("Overview"))
#     frame_disk.pack(pady=25)


#     # CPU
#     cpu_label = CTkLabel(frame_cpu, text=f'CPU usage: {psutil.cpu_percent()}%')
#     cpu_label.pack()

#     cpu_progressbar = CTkProgressBar(frame_cpu)
#     cpu_progressbar.pack(padx=20)


#     # RAM
#     ram_label = CTkLabel(frame_ram, text=f'RAM usage: {psutil.virtual_memory().percent}%')
#     ram_label.pack()

#     ram_progressbar = CTkProgressBar(frame_ram)
#     ram_progressbar.pack(padx=20)


#     # DISK
#     disk_label = CTkLabel(frame_disk, text=f'Disk usage: {psutil.disk_usage("/").percent}%')
#     disk_label.pack()

#     disk_progressbar = CTkProgressBar(frame_disk)
#     disk_progressbar.pack(padx=20)


#     # Inputbox
#     entry = CTkEntry(tabview.tab("Processes"))
#     entry.pack(pady=10)


#     # Suchbutton erstellen
#     search_button = CTkButton(tabview.tab("Processes"), text="Suchen", command=search)
#     search_button.pack(pady=10)


#     # Task list
#     # Create a listbox to display the processes
#     process_listbox = CTkListbox(tabview.tab("Processes"))
#     process_listbox.pack(pady=10)


#     # threading
#     process_list_thread = threading.Thread(target=lambda: update_tasklist())
#     process_list_thread.start()
#     print('[log] started a thread for process list update')

    

#     # Button zum Anzeigen der Prozessinformationen erstellen ENGLISH PLZ 😭
#     show_info_button = CTkButton(tabview.tab("Processes"), text="Prozess-Info abrufen", command=show_process_info)
#     show_info_button.pack(pady=10)


#     # update loop
#     update()

#     # root mainloop
#     root.mainloop()

# Look how cool is to put your program in a class ;)  
class GUI(CTk):
    def __init__(self):
        super().__init__()
        self.title('CrossTask')
        self.geometry("600x800")
        self.iconbitmap(os.path.join(os.getcwd(), 'img', 'bitmap.ico'))
        self.rowconfigure((0), weight=1)
        self.columnconfigure((0), weight=1)
        self.tabview = CTkTabview(self)
        self.tabview.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)
        self.tabview.add('Processes')
        self.tabview.add('Performance') #i think performance sounds better than overview
        self.tabview.set('Processes')
        self._performanceTab('Performance')
        self.autoupdate = True
        self.update_thread = threading.Thread(target=self.__update_performance_info)
        self.update_thread.daemon = True
        self.update_thread.start()


    def _processesTab(self, tabName:str):
        ...
    def _performanceTab(self, tabName:str):
        self.tabview.tab(tabName).rowconfigure((0,1,2,3,4,5), weight=1)
        self.tabview.tab(tabName).columnconfigure((0), weight=1)
        
        # CPU
        self.cpu_frame = self.__performanceBaseFrame('CPU Usage', self.tabview.tab(tabName))
        self.cpu_frame.grid(row=0, column=0, sticky=NSEW, padx=10, pady=20)
        
        # GPU
        # self.gpu_frame = self.__performanceBaseFrame('GPU Usage', self.tabview.tab(tabName))
        # self.gpu_frame.grid(row=1, column=0, sticky=NSEW, padx=10, pady=20)
        
        # RAM
        self.ram_frame = self.__performanceBaseFrame('Memory Usage', self.tabview.tab(tabName))
        self.ram_frame.grid(row=1, column=0, sticky=NSEW, padx=10, pady=20)
        
        # DISK
        for index, disk in enumerate(psutil.disk_partitions()):
            tmpFrame = self.__performanceBaseFrame(f'Disk Usage ( {disk.mountpoint} )', self.tabview.tab(tabName))
            # self.disk_frame = self.__performanceBaseFrame('Disk Usage', self.tabview.tab(tabName))
            tmpFrame.grid(row=2+index, column=0, sticky=NSEW, padx=10, pady=20)
            tmpFrame.bar.set(psutil.disk_usage(disk.mountpoint).percent/100)
            tmpFrame.text.configure(text=f'{psutil.disk_usage(disk.mountpoint).percent}%')
   
    def __performanceBaseFrame(self, title:str, master): #This bad boy will do all the performance frames you need >:)
        frame = CTkFrame(master, corner_radius=10)
        frame.rowconfigure((0,1), weight=1)
        frame.columnconfigure((0), weight=4)
        frame.columnconfigure((1), weight=1)
        CTkLabel(frame, text=title, font=('Arial', 16)).grid(row=0, column=0, sticky=W, padx=10, pady=10)
        frame.bar = CTkProgressBar(frame)
        frame.bar.set(0)
        frame.bar.grid(row=1, column=0, sticky=EW, padx=10, pady=(0, 20))
        frame.text = CTkLabel(frame, text='%%', font=('Arial', 16))
        frame.text.grid(row=0, column=1, rowspan=2)
        return frame
    def __update_performance_info(self):
        while self.autoupdate == True:
            cpuUsage = psutil.cpu_percent(interval=1)
            ramUsage = psutil.virtual_memory().percent
            self.cpu_frame.bar.set(cpuUsage/100)
            self.cpu_frame.text.configure(text=f'{cpuUsage}%')
            self.ram_frame.bar.set(ramUsage/100)
            self.ram_frame.text.configure(text=f'{ramUsage}%')

        
