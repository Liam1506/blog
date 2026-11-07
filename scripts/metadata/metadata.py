from pathlib import Path

from constants import *

class Metadata:
   def __init__(self, name: str, date: str, fileName: str, publish: bool):
      self.name = name
      self.date = date
      self.htmlFileName = ENTRIES_NAME + fileName + "/"
      self.publish = publish