import markdown
import os
from constants import *
from pathlib import Path
from scripts.buildIndex import *
import shutil
from scripts.metadata.getMetadata import getMetadata

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
   foldersToPublish = []
   clearEntries()
   moveStyles()
   for folder in folders:
      metadata = getMetadata(folder)
      if not metadata.publish:
         continue
      foldersToPublish.append(folder)

      path = Path(RAW) / Path(folder)
      filePath = path / Path(TEXT_FILE_NAME)
      fileNameOutput = folder+".html"



      outputName = Path(ENTRIES) / Path(fileNameOutput)

      outputName.parent.mkdir(parents=True, exist_ok=True)
      

      blogTemplate = imreadFile(BLOG_TEMPLATE)
      with open(filePath, "r", encoding="utf-8") as f:
         mdHtml = markdown.markdown(f.read())


      blogTemplate = updateTemplate(key="content", template=blogTemplate,updateValue=mdHtml)

      blogTemplate = updateTemplate(key="title", template=blogTemplate,updateValue=metadata.name)

      blogTemplate = updateTemplate(key="footer", template=blogTemplate,updateValue=imreadFile(FOOTER_PATH))

      with open(outputName, "w", encoding="utf-8") as f:
         f.write(blogTemplate)
   buildIndex(paths= foldersToPublish)

if __name__ == "__main__":
   main()