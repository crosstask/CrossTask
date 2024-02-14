# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import os

def check_dir():
    dokumente_pfad = os.path.join(os.path.expanduser('~'), 'Documents')

    if os.path.exists(os.path.join(dokumente_pfad, 'CrossTask')):
        print("[log] CrossTask configuration folder exists")
        return True
    else:
        print("[log] CrossTask configuration folder doesn't exists")
        return False