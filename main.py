# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from src.gui import GUI
from src.cli import cli
import sys

if len(sys.argv) > 1:
    cli()

else:
    app = GUI()
    app.mainloop()