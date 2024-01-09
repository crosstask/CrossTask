# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0


###########
# MODULES #
###########
from customtkinter import *
from CTkListbox import CTkListbox
import psutil
import os
import threading
import time
from PIL import Image



#######
# GUI #
#######
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
        self.tabview.add('Performance')
        self.tabview.add('About')
        self.tabview.set('Processes')
        self.autoupdate = True
        self.processListVar = StringVar(value=['Process list'])
        self._processesTab('Processes')
        self._performanceTab('Performance')
        currentTabAction = threading.Thread(target=self.__current_tab_action)
        currentTabAction.daemon = True
        currentTabAction.start() 

    def _processesTab(self, tabName:str):
        self.tabview.tab(tabName).rowconfigure((0, 2), weight=1)
        self.tabview.tab(tabName).rowconfigure((1), weight=5)
        self.tabview.tab(tabName).columnconfigure((0), weight=1)
        self.searchbar = CTkEntry(self.tabview.tab(tabName), font=('Arial', 20), height=50) 
        self.processList = CTkListbox(self.tabview.tab(tabName), listvariable=self.processListVar)
        self.searchbar.grid(row=0, column=0, sticky='EW', padx=30, pady=10)
        self.processList.grid(row=1, column=0, sticky='NSEW', padx=30, pady=10)
        self.updateProcessesBtn = CTkButton(self.tabview.tab(tabName), text='Refresh', font=('Arial', 16), command=lambda:update())
        self.updateProcessesBtn.grid(row=2, column=0, sticky='NS', padx=40)
        def update():
            self.autoupdate = True

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
   
    def aboutTab(self, tabName:str):
        logo = CTkImage(Image.open("./content/logo_crosstask-removebg.png"), size=(500, 500))
        ...
    def __performanceBaseFrame(self, title:str, master):
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
        while self.autoupdate == True and self.tabview.get() == 'Performance':
            cpuUsage = psutil.cpu_percent(interval=1)
            ramUsage = psutil.virtual_memory().percent
            self.cpu_frame.bar.set(cpuUsage/100)
            self.cpu_frame.text.configure(text=f'{cpuUsage}%')
            self.ram_frame.bar.set(ramUsage/100)
            self.ram_frame.text.configure(text=f'{ramUsage}%')

    def __update_process_list(self):
        while self.autoupdate == True and self.tabview.get() == 'Processes':
          self.processListVar.set([process.name() for process in psutil.process_iter()])
          self.autoupdate = False
    def __current_tab_action(self):
        # For optimisation: depending on the tab the user is it starts/stops the actions on it, making the program lightweight
        while(True):
            currentTab = self.tabview.get()
            if currentTab == 'Performance':
                self.autoupdate = True
                update_thread = threading.Thread(target=self.__update_performance_info)
                update_thread.daemon = True
                update_thread.start() 
                update_thread.join()
            time.sleep(0.25)
            if currentTab == 'Processes':
                if self.autoupdate == True:    
                    self.updateProcessesBtn.configure(state='disabled')
                    update_thread = threading.Thread(target=self.__update_process_list)
                    update_thread.daemon = True
                    update_thread.start() 
                    update_thread.join()
                    self.updateProcessesBtn.configure(state='enabled')
            time.sleep(0.25)
