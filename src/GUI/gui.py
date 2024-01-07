import customtkinter
import psutil

def main_gui():
    def update():
        # CPU
        cpu_label.configure(text=f'CPU usage: {psutil.cpu_percent()}%')
        cpu_progressbar.set(psutil.cpu_percent()/100)

        # RAM
        ram_label.configure(text=f'RAM usage: {psutil.virtual_memory().percent}%')
        ram_progressbar.set(psutil.virtual_memory().percent/100)

        # DISK
        disk_label.configure(text=f'Disk usage: {psutil.disk_usage('/').percent}%')
        disk_progressbar.set(psutil.disk_usage('/').percent/100)


        root.after(1000, update)

        

    root = customtkinter.CTk()
    root.geometry('290x400')
    root.title('CrossTask')


    # Create Frames
    frame_cpu = customtkinter.CTkFrame(root)
    frame_cpu.pack(pady=10)

    frame_ram = customtkinter.CTkFrame(root)
    frame_ram.pack(pady=10)

    frame_disk = customtkinter.CTkFrame(root)
    frame_disk.pack(pady=10)


    # CPU
    cpu_label = customtkinter.CTkLabel(frame_cpu, text=f'CPU usage: {psutil.cpu_percent()}%')
    cpu_label.pack()

    cpu_progressbar = customtkinter.CTkProgressBar(frame_cpu)
    cpu_progressbar.pack(pady=15, padx=20)


    # RAM
    ram_label = customtkinter.CTkLabel(frame_ram, text=f'RAM usage: {psutil.virtual_memory().percent}%')
    ram_label.pack()

    ram_progressbar = customtkinter.CTkProgressBar(frame_ram)
    ram_progressbar.pack(pady=15, padx=20)


    # DISK
    disk_label = customtkinter.CTkLabel(frame_disk, text=f'Disk usage: {psutil.disk_usage('/').percent}%')
    disk_label.pack()

    disk_progressbar = customtkinter.CTkProgressBar(frame_disk)
    disk_progressbar.pack(pady=15, padx=20)

    # update loop
    update()

    # root mainloop
    root.mainloop()