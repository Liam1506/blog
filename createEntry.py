import os
import json
import datetime
import re
from pathlib import Path
from constants import *


def sanitize_filename(name):
    clean = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '-')
    return clean or "untitled_article"

def createMetadata(name, date, folder_path):
    data = {
        "name": name,
        "date": str(date),
    }
    file_path = folder_path / "metadata.json"
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def createFile(folder_path, date):
    file_path = folder_path / "text.md"
    with open(file_path, "w") as f:
        f.write(f"{date}\n\n")

def main():
    nameOfArticle = input("Name of the article: ")
    date = datetime.datetime.now()
    
    safe_name = sanitize_filename(nameOfArticle)
    
    article_folder = Path(raw) / safe_name

    if article_folder.exists():
        print(f"Error: The folder '{safe_name}' already exists.")
        return
    article_folder.mkdir(parents=True, exist_ok=True)
    
    createMetadata(nameOfArticle, date, article_folder)
    createFile(article_folder, date)
    
    print("\nCreation successful")
    print(f"Start writing under: {article_folder.resolve() / 'text.md'}")

if __name__ == "__main__":
    main()