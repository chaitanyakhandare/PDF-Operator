
import datetime

import os, PyPDF2
from PyPDF2 import PdfReader, PdfMerger


# Getting date & time
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
outputFILE = f"{hour}.{minute}.{second}-merged.pdf"



def extractText():
    src = input("Enter full path of you document: ")
    pageNumber = int(input("Enter page number to extract text: "))
    
    reader = PdfReader(src)

    pageToExtract = reader.pages[(pageNumber-1)]
    extractedData = str(pageToExtract.extract_text())

    pathOfTxt = "/Users/chaitanyakhandare/Developer/CODE/Python/Projects Python/PDF Merger/extractedText.txt"

    # writing data in file
    fp = open(pathOfTxt, "w")
    fp.write(extractedData)
    fp.close()

    # speak result
    os.system(f"say Your extracted data is stored in extractedText dot txt file")
    print("Your extracted data is stored in extractedText.txt file")




def mergerPDF():
    # It merges only pdfs, so give input of PDF files only!

    merger = PdfMerger()

    # taking input & storing in variable as list
    filesToMerge = []

    while True:
        inputFiles = input("Enter full paths of file to be merge (to stop type: exit): ")
        if inputFiles == "exit":
            break
        filesToMerge.append(inputFiles)

    # merging files
    for f in filesToMerge:
        if f == "":
            continue
        else:
            merger.append(f)

    merger.write(outputFILE)
    merger.close()

    print("DONE merging")
    
    # speak result
    os.system(f"say 'All your {len(filesToMerge)} files are merged successfully.'")
    print("All your files are merged successfully merged.")
    print("* * * * * * * \n")

    # Use this examples to try code:
    example1 = "/Users/chaitanyakhandare/Documents/My DOCS/Light bill Manchar.pdf"
    example2 = "/Users/chaitanyakhandare/Documents/My DOCS/Acko Bike Policy - ABTA00859401755_00.pdf"
    example3 = "/Users/chaitanyakhandare/Documents/My DOCS/60 days of Fitness Boldfit.pdf"
    





print("* * * * * * * * * * * * * * * * *")
print("*    Welcome to PDF Operator    *")
print("* * * * * * * * * * * * * * * * *")
print("\n")


while True:
    print("Features: ")
    print("1. PDF Text Extract")
    print("2. PDF Merger")
    print("99. Exit\n")

    userInput = int(input("Please choose feature: "))

    if userInput == 99:
        break
    else:
        match userInput:
            case 1:
                extractText()
            case 2:
                mergerPDF()
            


