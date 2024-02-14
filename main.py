# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

from src.gui import GUI
from src.cli import cli
from src.functions.check_dir import check_dir
from src.functions.struct import struct
import sys

if len(sys.argv) > 1:
    cli()
else:
    actual_structure = check_dir()
    if not actual_structure:
        struct()

    # start graphical user interface
    app = GUI()
    app.mainloop()
