# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from src.gui import GUI
from src.cli import cli
import sys

if len(sys.argv) > 1:
    cli()

else:
    try:
        app = GUI()
        app.mainloop()
    except Exception as e:
        print(e)