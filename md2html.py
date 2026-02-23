import markdown
import os
from constants import *

def main():

   files = os.listdir('raw')
   for filename in files:
      print (filename)
      markdown.markdownFromFile(input=raw+filename, output=entries+filename.replace('.md', '.html'))

if __name__ == "__main__":
   main()