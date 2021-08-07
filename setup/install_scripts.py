import shutil
import os

from constants import * 

# Create install location
dir = os.path.dirname(INSTALL_LOCATION)
if not os.path.exists(dir):
    os.makedirs(dir)

for file in os.listdir(SCRIPT_LOCATION) :
    shutil.copy(os.path.join(SCRIPT_LOCATION, file), INSTALL_LOCATION)