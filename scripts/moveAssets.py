from pathlib import Path
import shutil
from constants import *
import os

def moveAssets(name: str):
   assetPath = Path(RAW) / Path(name) / ASSETS_FOLDER
   if(os.path.isdir(assetPath)):
      shutil.copytree(assetPath, ASSETS_ENTRIES_FOLDER, dirs_exist_ok=True)
