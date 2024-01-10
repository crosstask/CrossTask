# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import argparse
import psutil 

def cli():
    parser = argparse.ArgumentParser(description='CLI of CrossTask with command-line options')

    parser.add_argument('--get', '-g', nargs='*', help='Get the percentage of CPU/RAM used')

    args = parser.parse_args()

    if args.get:
        for arg in args.get:
            if arg.lower() == 'cpu':
                print(psutil.cpu_percent(1))
            elif arg.lower() == 'ram':
                print(psutil.virtual_memory().percent)
            else:
                print(f'\nStat not found "{arg}", avaiable options:\n    cpu\n    ram')
                for disk in psutil.disk_partitions():
                    print(f'    {disk.mountpoint}')



