from pathlib import Path
from constants import *
from scripts.helper.updateTemplate import *
from scripts.metadata.getMetadata import * 

def buildIndex(paths: list[str]):
    print(f"Processing {len(paths)} paths...")
    data_items = []
    for p in paths:
        data_items.append({
            "path": p,
            "metadata": getMetadata(p)
        })
    data_items.sort(key=lambda x: x["metadata"].date, reverse=True)

    linksHtml = ""
    preLoadHtml = ""

    linkTemplate = imreadFile(LINK_TEMPLATE)
    prefetchTemplate = imreadFile(PREFETCH_TEMPLATE)
    indexTemplate = imreadFile(INDEX_TEMPLATE)

    for index, item in enumerate(data_items):
        meta = item["metadata"]
        
        clean_date = meta.date[:16]

        temp_link = updateTemplate(key="link", updateValue=meta.htmlFileName, template=linkTemplate)
        temp_link = updateTemplate(key="name", updateValue=meta.name, template=temp_link)
        temp_link = updateTemplate(key="index", updateValue=str(index + 1), template=temp_link)
        temp_link = updateTemplate(key="date", updateValue=clean_date, template=temp_link)
        linksHtml += temp_link

        temp_prefetch = updateTemplate(key="link", updateValue=meta.htmlFileName, template=prefetchTemplate)
        preLoadHtml += temp_prefetch

    indexHTML = updateTemplate(key="links", updateValue=linksHtml, template=indexTemplate)
    indexHTML = updateTemplate(key="prefetch", updateValue=preLoadHtml, template=indexHTML)


    indexHTML = updateTemplate(key="footer", updateValue=imreadFile(FOOTER_PATH), template=indexHTML)
    indexHTML = updateTemplate(key="header", updateValue=imreadFile(HEADER_PATH), template=indexHTML)

    with open(SERVE_PATH + "index.html", "w") as f:
        f.write(indexHTML)
    
    print(f"Successfully wrote index to {SERVE_PATH}index.html")

def imreadFile(templatePath):
    with open(templatePath, "r") as f:
        return f.read()
   
