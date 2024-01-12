# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import argparse
import psutil 

def cli():
    parser = argparse.ArgumentParser(description='CLI of CrossTask')

    parser.add_argument('--get', '-g', nargs='*', help='Get the percentage of CPU/RAM used')

    args = parser.parse_args()

    if args.get:
        for arg in args.get:
            if arg.lower() == 'cpu':
                print(f'CPU usage: {psutil.cpu_percent(1)}%')
            elif arg.lower() == 'ram':
                print(f'RAM usage: {psutil.virtual_memory().percent}%')
            else:
                print(f'\nStat not found "{arg}", avaiable options:\n    cpu\n    ram')
                for disk in psutil.disk_partitions():
                    print(f'    {disk.mountpoint}')
