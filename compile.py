import markdown
import os
from constants import *
from pathlib import Path
from scripts.buildIndex import *
import shutil
from scripts.metadata.getMetadata import getMetadata

def moveStyles():
   pathServe = Path(SERVE_PATH)/ Path(STYLES)
   stylesPathOld = Path(TEMPLATE_PATH)/ Path(STYLES)
   shutil.copytree(str(stylesPathOld), pathServe, dirs_exist_ok=True)

def clearEntries():
    cname_content = ""
    if os.path.isfile(CNAME):
        cname_content = imreadFile(CNAME)
    
    if os.path.exists(SERVE_PATH):
        shutil.rmtree(SERVE_PATH)
    
    os.makedirs(SERVE_PATH, exist_ok=True)
    
    with open(CNAME, "w") as f:
        f.write(cname_content)


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
         mdHtml = markdown.markdown(
             f.read(),
             extensions=[
                  'tables',
                  'fenced_code',
                  'extra',
                  'toc',
                  'codehilite',          
                  'footnotes',           
                  'admonition',          
                  'pymdownx.superfences',
                  'pymdownx.tasklist',  
                  'pymdownx.magiclink', 
                  'pymdownx.caret',
               ],
             extension_configs={
                 'toc': {
                     'permalink': True, 
                     'baselevel': 1,
                 },
                 'pymdownx.tasklist': {
                     'custom_checkbox': True, 
                 },
                 'codehilite': {
                     'css_class': 'highlight',
                     'guess_lang': True      
                 }
             
             }
         )

      blogTemplate = updateTemplate(key="content", template=blogTemplate, updateValue=mdHtml)
      blogTemplate = updateTemplate(key="title", template=blogTemplate, updateValue=metadata.name)
      blogTemplate = updateTemplate(key="footer", template=blogTemplate, updateValue=imreadFile(FOOTER_PATH))
      blogTemplate = updateTemplate(key="header", template=blogTemplate, updateValue=imreadFile(HEADER_PATH))

      with open(outputName, "w", encoding="utf-8") as f:
         f.write(blogTemplate)
   
   buildIndex(paths=foldersToPublish)

if __name__ == "__main__":
   main()