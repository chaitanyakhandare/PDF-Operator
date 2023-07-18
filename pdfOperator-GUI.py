
import datetime

import tkinter
from tkinter import Menu, StringVar, Frame, Label
from tkmacosx import Button
from tkinter import filedialog as fd
from tkPDFViewer import tkPDFViewer

import os, PyPDF2
from PyPDF2 import PdfReader, PdfMerger

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




def mergerPDF(fileList):
    # It merges only pdfs, so give input of PDF files only!

    merger = PdfMerger()

    # taking input & storing in variable as list
    # filesToMerge = []
    # while True:
    #     inputFiles = input("Enter full paths of file to be merge (to stop type: exit): ")
    #     if inputFiles == "exit":
    #         break
    #     filesToMerge.append(inputFiles)

    # merging files
    for f in fileList:
        if f == "":
            continue
        else:
            merger.append(f)

    merger.write(outputFILE)
    merger.close()

    print("DONE merging")
    
    # speak result
    os.system(f"say 'All your {len(fileList)} files are merged successfully.'")
    # print("All your files are merged successfully with name files-all-merged.pdf")

    # Use this examples to try code:
    example1 = "/Users/chaitanyakhandare/Documents/My DOCS/Light bill Manchar.pdf"
    example2 = "/Users/chaitanyakhandare/Documents/My DOCS/Acko Bike Policy - ABTA00859401755_00.pdf"
    example3 = "/Users/chaitanyakhandare/Documents/My DOCS/60 days of Fitness Boldfit.pdf"
    



# Getting date & time
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
outputFILE = f"{year}-{month}-{day}-{hour}.{minute}-merged.pdf"


# tkinter code from here
root = tkinter.Tk()
root.geometry("838x556")
root.minsize(575, 300)
root.title("PDF Operator")

menubar = Menu(root)

fileList = []

nameOfLast = StringVar()

def openFile():
    filename = fd.askopenfilename()
    if ".pdf" in filename:
        fileList.append(filename)
        nameOfLast.set(filename)
    else:
        os.system("say 'please choose pdf files only'")


def mergingFunc():
    mergerPDF(fileList)
    print("Starting merging")


# Adding Menubar
menuButtons = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Features', menu = menuButtons)
menuButtons.add_command(label="Extract Text")
menuButtons.add_command(label="PDF Merger")
menuButtons.add_separator()
menuButtons.add_command(label="Quit", command=root.destroy)



# frame - 1
frame1 = Frame(root, borderwidth=3, highlightbackground="white", highlightcolor="white", highlightthickness=1, bd=0)
frame1.pack(side="top", padx=10, pady=40)

text = Label(frame1, text="Welcome to PDF Operator", padx=20, pady=13, font='helvetica 18 bold')
text.grid(row=0, column=0)

buttonOpen = Button(frame1, text="Open file", command=openFile)
buttonOpen.grid(row=0, column=1, padx=10, pady=20)

buttonMerge = Button(frame1, text="Start Merging", font='helvetica 14', command=mergingFunc, bg="#64DD17")
buttonMerge.grid(row=0, column=2, padx=20)



# frame - 2
frame2 = Frame(root, borderwidth=3, highlightbackground="white", highlightcolor="white", highlightthickness=1, bd=0)
frame2.pack(padx=20, pady=20)

text2Last = Label(frame2, text="Last file selected is: ", font='roboto.mono 14')
text2Last.grid(row=0, column=0)

text3LastFile = Label(frame2, textvariable=nameOfLast, font='helvetica 14 bold')
text3LastFile.grid(row=0, column=1, padx=20, pady=20)

text4Willbe = Label(frame2, text="Merged file name will be: ", font='helvetica 14')
text4Willbe.grid(row=1, column=0, padx=20)

text5WillbeFile = Label(frame2, text=outputFILE, font='helvetica 14 bold')
text5WillbeFile.grid(row=1, column=1, padx=20, pady=20)




# frame - 3
frame3 = Frame(root)
frame3.pack(padx=20, pady=20)

text_caution = Label(frame3, text="Please restart the app to merge PDFs again.", font='helvetica 14 bold')
text_caution.config(foreground="orange")
text_caution.pack()



root.config(menu = menubar)

root.mainloop()
print(fileList)




# extractText()

# mergerPDF()


