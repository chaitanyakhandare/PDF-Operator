
import datetime

import os, PyPDF2
from PyPDF2 import PdfReader, PdfMerger
from PyPDF2 import PdfWriter
import img2pdf 



# Getting date & time
current_time = datetime.datetime.now()
hour = current_time.hour
minute = current_time.minute
second = current_time.second
outputFileName = f"{hour}.{minute}.{second}-merged.pdf"



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

    pm = PdfMerger()

    # taking input & storing in variable as list
    filesToMerge = []

    while True:
        inputFiles = input("Enter full paths of file to be merge (to stop type: exit): ")

        if inputFiles == "exit":
            print(filesToMerge)
            break
        else:
            extention = os.path.splitext(inputFiles)
            if extention[1] == ".pdf":
                filesToMerge.append(inputFiles)
            else:
                os.system("say 'please choose pdf files only'")
            

    # checking empty list
    if filesToMerge == []:
        print("\nPlease select some files !")
        print("* * * * * * * \n")
    else:
        # merging files
        for f in filesToMerge:
            if f == "":
                continue
            else:
                pm.append(f)

        pm.write(outputFileName)
        pm.close()

        print("DONE merging")

        # speak result
        os.system(f"say 'All your {len(filesToMerge)} files are merged successfully.'")
        print("All your files are merged successfully.")
        print("* * * * * * * \n")

    # Use this examples to try code:
    example1 = "/Users/chaitanyakhandare/Documents/My DOCS/Light bill Manchar.pdf"
    example2 = "/Users/chaitanyakhandare/Documents/My DOCS/Acko Bike Policy - ABTA00859401755_00.pdf"
    example3 = "/Users/chaitanyakhandare/Documents/My DOCS/60 days of Fitness Boldfit.pdf"
    



def splitPdfPages():

    pdf_document = ""
    pageNumber = []
    
    while True:
        userInput = input("Enter PATH of pdf file: ")

        extention = os.path.splitext(userInput)
        if extention[1] == ".pdf":
            pdf_document = userInput
            break
        else:
            os.system("say 'please choose pdf files only'")
            print(pdf_document)

    print(pdf_document)
    print("")

    while True:
        inputPage = input("Enter PAGE NUMBERS to split (type 'done' to end): ")

        if inputPage == "done":
            break
        else:
            inputPage = int(inputPage)
            if isinstance(inputPage, int):
                if inputPage > 0:
                    pageNumber.append(inputPage - 1)
                else:
                    os.system("say 'invalid page number'")
            else:
                os.system("say 'invalid input'")


    with open(pdf_document, "rb") as infile:

        reader = PdfReader(pdf_document)
        writer = PdfWriter()

        for p in pageNumber:
            writer.add_page(reader.pages[p])

        with open(outputFileName.format(pageNumber), 'wb') as outfile:
            writer.write(outfile)


            


def imageToPdf():
    # taking input & storing in variable as list
    filesToMerge = []

    # making list of files
    while True:
        inputFiles = input("Enter full paths of file to be merge (to stop type: exit): ")

        if inputFiles == "exit":
            print(filesToMerge)
            break
        else:
            extention = os.path.splitext(inputFiles)

            if extention[1] == ".jpg":
                filesToMerge.append(inputFiles)
            if extention[1] == ".jpeg":
                filesToMerge.append(inputFiles)
            if extention[1] == ".png":
                filesToMerge.append(inputFiles)
            else:
                os.system("say 'please choose image files only'")


    # checking empty list
    if filesToMerge == []:
        print("\nPlease select some files !")
        print("* * * * * * * \n")
    else:
        fp = open(outputFileName, "wb")
        converting  = img2pdf.convert(filesToMerge)
        fp.write(converting) # IGNORE warning!
        fp.close()

        print("\nDONE Converting and Merging")

        # speak result
        os.system(f"say 'All your {len(filesToMerge)} files are converted and merged successfully.'")
        print("All your files are converted successfully.")
        print("* * * * * * * \n")


    # Use this examples to try code:
    example1 = "/Users/chaitanyakhandare/Downloads/Screenshot 2023-06-13 at 11.22.39 PM.png"
    example2 = "/Users/chaitanyakhandare/Downloads/Chaitanya ID Card MITWPU.jpg"
    example3 = "/Users/chaitanyakhandare/Documents/My DOCS/60 days of Fitness Boldfit.pdf"
    




# * * * * *   M A I N   * * * * * #

if __name__ == "__main__":

    print("\n")
    print("* * * * * * * * * * * * * * * * *")
    print("*    Welcome to PDF Operator    *")
    print("* * * * * * * * * * * * * * * * *")
    print("\n")


    while True:
        print("Features: ")
        print("1. PDF Text Extracter")
        print("2. PDF Merger")
        print("3. Image to PDF converter (can do merge also)")
        print("4. Split PDF Pages")
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
                case 3:
                    imageToPdf()
                case 4:
                    splitPdfPages()
                


