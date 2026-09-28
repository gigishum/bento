# bentoPaths.py

"""
Locations of BENTO's local data files (config.json, bento.db, color_profiles.txt).

They all live in the BENTO folder itself -- the folder containing src/ -- rather
than in the user's home directory, so a BENTO folder carries its own metadata.
"""

from os.path import abspath, dirname, join

# src/db/bentoPaths.py -> src/db -> src -> BENTO folder
BENTO_DIR = dirname(dirname(dirname(abspath(__file__))))
CONFIG_PATH = join(BENTO_DIR, 'config.json')
DB_PATH = join(BENTO_DIR, 'bento.db')
COLOR_PROFILES_PATH = join(BENTO_DIR, 'color_profiles.txt')
