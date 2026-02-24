from constants import *
from .metadata import *
import json
from pathlib import Path

def getMetadata(fileName: str) -> Metadata:
   path = Path(RAW) / fileName / Path(METADATA_FILE_NAME)
   with open(path, "r") as f:
      jsonData = json.loads(f.read())
      print(jsonData)
   return Metadata(name=jsonData["name"],  date=jsonData["date"], fileName=fileName,publish=jsonData["publish"])

