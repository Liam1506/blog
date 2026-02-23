from constants import * 

def buildIndex(paths: list):
   print(paths)
   linksHtml = ""
   linkTemplate = imreadFile(LINK_TEMPLATE)
   print("IMREAD")
   for path in paths:
      temp = updateTemplate(key="link",updateValue=path, template=linkTemplate)
      temp = updateTemplate(key="name",updateValue=path, template=temp)
      linksHtml = linksHtml + temp

   print(linksHtml)

   indexTemplate = imreadFile(INDEX_TEMPLATE)
   indexHTML = updateTemplate(key="links",updateValue=linksHtml, template=indexTemplate)

   with open(SERVE_PATH+"index.html", "w") as f:
      f.write(indexHTML)

def imreadFile(templatePath):
   print("TP")
   print(templatePath)
   with open(templatePath, "r") as f:
      return f.read()
   
def updateTemplate(key, template, updateValue):
   return template.replace("{{"+key+"}}", str(updateValue))