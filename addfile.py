import os
import shutil as sh
import csv
import sys
import argparse

## loop to create folders if they don't exist 

for subdirectory in ["files/images" , "files/docs" , "files/audio"]:
    if not os.path.isdir(subdirectory):
        os.makedirs(subdirectory)

source_folder = "files/"
destination_images = "files/images/"
destination_docs = ("files/docs/")
destination_audio = ("files/audio/")

## recap

if os.path.isfile("files/recap.csv"):
    verify = "a"

else:
    verify = "w"

header = ["name" , "type" , "size"]
    
recap = open("files/recap.csv" , verify , newline = "")
w = csv.writer(recap)

if verify == "w":
    w.writerow(header)
    
## 3 tuple divided in which add the extensions

extensions_image = (".jpg" , ".jpeg" , ".png")
extensions_docs = (".txt" , ".odt")
extensions_audio = (".mp3")
    
## useful in the next list comprehension   

folders_tuple = ("images" , "docs" , "audio")

## creating a list based on os.listdir we avoid to include folders and recap file in the choices argument

file_list = [file for file in os.listdir("files") if not file.endswith(folders_tuple) and file != "recap.csv"]

def move(args):
        
    file = args.file    
    
    source = source_folder + file
    place_images = destination_images + file
    place_docs = destination_docs + file
    place_audio = destination_audio + file
    
    ## recap rows
    
    name , extension = os.path.splitext(file)
    data_images = [[name , "image" , os.path.getsize(source)]]
    data_docs = [[name , "doc" , os.path.getsize(source)]]
    data_audio = [[name , "audio" , os.path.getsize(source)]]
        
    ## conditionals to update recap and move file 
        
    if file.endswith(extensions_image):
        w.writerows(data_images)
        sh.move(source , place_images)
            
    elif file.endswith(extensions_docs):
        w.writerows(data_docs)
        sh.move(source , place_docs)
            
    elif file.endswith(extensions_audio):
        w.writerows(data_audio)
        sh.move(source , place_audio)
    
    ## i could use --else-- to print an error message, but it appears anyway thanks to argument --choices--
    
    ## this text will be printed only if a file is moved, we don't need the if statement
    
    print("file moved")
    
def main():
    parser = argparse.ArgumentParser("organize file")
    parser.add_argument("file", choices = file_list , nargs = "?", type = str, help = "write the file you want to move")
    
    args = parser.parse_args()

    sys.stdout.write(str(move(args)))
    
main()