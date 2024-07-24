import glob
import os
import zipfile
from pathlib import Path

# Path where you download or store the zip file.
p = Path('C:\\Users\\freak\\Downloads')

# Directory where the game stores its mods.
directory = 'D:\\World_of_Tanks_EU\\mods\\'

# Gets the newest added folder in the selected mod directory. For example:
# The game adds a new update every week and the mod has to be configured to the current game version to work.
# That is why it is required to select the last folder in a directory.
newest_patch = max(glob.glob(os.path.join(directory, '*/')), key=os.path.getmtime)

# We iterate over the selected path above (where we download or store our zip files)
# As long as we have only one (the zip file we want to use) in that folder we do not need to specify it's name every time
# This way we can freely run the script any time we want without any corrections.
for f in p.glob('*.zip'):
    with zipfile.ZipFile(f, 'r') as archive:
        archive.extractall(path=newest_patch)
        print('Enjoy your modded gaming experience.')
