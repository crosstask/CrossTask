# CrossTask Team
# Developers: @zlElo and @DarkGloves
# Licensed under GPL 3.0

import os
import json


def struct():
    cross_task_path = os.path.join(os.path.expanduser('~'), 'Documents', 'CrossTask')
    os.makedirs(cross_task_path, exist_ok=True)
    settings_path = os.path.join(cross_task_path, 'Settings')
    os.makedirs(settings_path, exist_ok=True)
    json_file_path = os.path.join(settings_path, 'settings.json')

    json_content = {
        "version": "1.04",
        "theme": "System"
    }

    with open(json_file_path, 'w') as json_file:
        json.dump(json_content, json_file, indent=4)

    print("[log] created CrossTask configuration folder")