import markdown
import os
from constants import *
from pathlib import Path
from buildIndex import *
import shutil

def moveStyles():

   pathToRm = Path(SERVE_PATH)/ Path(STYLES)
   if  os.path.exists(pathToRm):
      for file in os.listdir(pathToRm):
         filePath = pathToRm / Path(file)
         os.remove(filePath)
      

   stylesPathOld = Path(TEMPLATE_PATH)/ Path(STYLES)



   

   shutil.copytree(str(stylesPathOld), pathToRm, dirs_exist_ok=True)

def clearEntries():
   for file in os.listdir(ENTRIES):

      filePath = Path(ENTRIES) / Path(file)
      
      os.remove(filePath)

def main():
   folders = os.listdir(RAW)
   clearEntries()
   moveStyles()
   htmlFilePaths = []
   for folder in folders:

       
      path = Path(RAW) / Path(folder)
      files = os.listdir(path) 

      for file in files:
         if file != "metadata.json":
            print(file)
            filePath = path / Path(file)
            fileNameOutput = file.replace('.md', '.html')



            outputName = Path(ENTRIES) / Path(fileNameOutput)

            outputName.parent.mkdir(parents=True, exist_ok=True)
           
            with open(filePath, "r", encoding="utf-8") as f:
               html = markdown.markdown(f.read())

            with open(BLOG_TEMPLATE, "r", encoding="utf-8") as f:
               template = f.read()
            finishedFile = template.replace("{{content}}", html)

            with open(outputName, "w", encoding="utf-8") as f:
               f.write(finishedFile)
            htmlFilePaths.append(Path(ENTRIES_NAME) / Path(fileNameOutput))
   buildIndex(paths=htmlFilePaths)

if __name__ == "__main__":
   main()