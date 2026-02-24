from pathlib import Path

from constants import *

class Metadata:
   def __init__(self, name: str, date: str, fileName: str, publish: bool):
      self.name = name
      self.date = date
      self.htmlFileName = Path(ENTRIES_NAME) / Path(fileName+".html")
      self.publish = publish