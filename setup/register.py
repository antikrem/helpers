from winreg import *
import os
import sys

from constants import * 

PYTHON_INSTALL = f'"{sys.executable}"'

MUIVerb = 'MUIVerb'
ExtendedSubCommandsKey = 'ExtendedSubCommandsKey'
Default = ''

def create_key(location) :
    return CreateKeyEx(
            HKEY_CLASSES_ROOT, 
            f'Directory\\{location}', 
            0, 
            KEY_ALL_ACCESS
        )

def add_value(key, name, value) :
    SetValueEx(key, name, 0, REG_SZ, value)

def register_extended_commands() :
    key = create_key('Background\\shell\\Helpers')
    add_value(key, MUIVerb, 'Helpers')
    add_value(key, ExtendedSubCommandsKey, 'Directory\\ContextMenus\\Helpers')

def register_command(command_name, label) :
    key = create_key(f'ContextMenus\\Helpers\\shell\\{command_name}')
    add_value(key, MUIVerb, label)

    key = create_key(f'ContextMenus\\Helpers\\shell\\{command_name}\\command')
    add_value(key, Default, f'{PYTHON_INSTALL} \"{INSTALL_LOCATION}\\{command_name}.py\"')

def get_command_label(file) :
    with open(os.path.join(SCRIPT_LOCATION, file)) as f:
        return f.readline()[1:].strip()

register_extended_commands()

for file in os.listdir(SCRIPT_LOCATION) :
    register_command(file.split(".")[0], get_command_label(file))