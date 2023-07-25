
import datetime, os, time
import img2pdf 

import tkinter
from tkinter import Menu, StringVar, Frame, Label, messagebox, Canvas
from tkmacosx import Button
from tkinter import filedialog as fd

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

    pm = PdfMerger()

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
            pm.append(f)

    pm.write(outputFileName)
    pm.close()

    print("DONE merging")
    
    # speak result
    os.system(f"say 'All your {len(fileList)} files are merged successfully.'")

    messagebox.showinfo("Great!", f"All your {len(fileList)} files are merged successfully.")
    # print("All your files are merged successfully with name files-all-merged.pdf")

    # Use this examples to try code:
    example1 = "/Users/chaitanyakhandare/Documents/My DOCS/Light bill Manchar.pdf"
    example2 = "/Users/chaitanyakhandare/Documents/My DOCS/Acko Bike Policy - ABTA00859401755_00.pdf"
    example3 = "/Users/chaitanyakhandare/Documents/My DOCS/60 days of Fitness Boldfit.pdf"
    

# # # # # #   def M E R G E   # # # # # 
def windowMerge():
    # tkinter code from here
    root = tkinter.Tk()
    root.geometry("838x556")
    root.minsize(681, 456)
    root.title("PDF Merger")

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
        time.sleep(1)
        root.destroy()
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

    text = Label(frame1, text="Welcome to PDF Merger", padx=20, pady=13, font='helvetica 18 bold')
    text.grid(row=0, column=0)

    buttonOpen = Button(frame1, text="Open file", height=40, width=110, command=openFile)
    buttonOpen.grid(row=0, column=1, padx=10, pady=20)

    buttonMerge = Button(frame1, text="Start Merging", font='helvetica 14', height=40, width=130, command=mergingFunc, bg="#64DD17")
    buttonMerge.grid(row=0, column=2, padx=20)



    # frame - 2
    frame2 = Frame(root, borderwidth=3, highlightbackground="white", highlightcolor="white", highlightthickness=1, bd=0)
    frame2.pack(padx=20, pady=20)

    text2Last = Label(frame2, text="Last file selected: ", font='monaco 14')
    text2Last.grid(row=0, column=0)

    text3LastFile = Label(frame2, textvariable=nameOfLast, font='helvetica 14 bold')
    text3LastFile.grid(row=0, column=1, padx=20, pady=20)

    text4Willbe = Label(frame2, text="Merged file name will be: ", font='monaco 14')
    text4Willbe.grid(row=1, column=0, padx=20)

    text5WillbeFile = Label(frame2, text=outputFileName, font='helvetica 14 bold')
    text5WillbeFile.grid(row=1, column=1, padx=20, pady=20)



    # frame - 3
    frame3 = Frame(root)
    frame3.pack(padx=20, pady=20)

    text_caution = Label(frame3, text="Please restart the app to merge PDFs again.", font='menlo 15 bold')
    text_caution.config(foreground="gold")
    text_caution.pack()


    root.config(menu = menubar)

    root.mainloop()
    print(fileList)



# # # # # #   def I M G 2 P D F   # # # # # 
def Img2PdfFUNC():
    windowImg2PDF = tkinter.Tk()
    windowImg2PDF.geometry("887x664")
    windowImg2PDF.minsize(887, 664)
    windowImg2PDF.title("Image to PDF Converter")
    windowImg2PDF.configure(bg="#FCFCFC")

    fileList1 = []
    nameOfLast = StringVar()

    def openImgFile():
        filename = fd.askopenfilename()
        filenameSPLIT = os.path.splitext(filename)
        
        if filenameSPLIT[1] == ".jpg":
            fileList1.append(filename)
            nameOfLast.set(filename)
        if filenameSPLIT[1] == ".jpeg":
            fileList1.append(filename)
            nameOfLast.set(filename)
        if filenameSPLIT[1] == ".png":
            fileList1.append(filename)
            nameOfLast.set(filename)
        else:
            os.system("say 'please choose image files only'")

        print(fileList1)


    def funcImg2Pdf(fileList1):
        fp = open(outputFileName, "wb")
        converting  = img2pdf.convert(fileList1)
        fp.write(converting) # ignore warning
        fp.close()

        print("\nDONE Converting and Merging")

        # speak result
        os.system(f"say 'All your {len(fileList1)} files are converted and merged successfully.'")
        messagebox.showinfo(title="Great!", message=f"All your {len(fileList1)} files are converted and merged successfully.")
        print("All your files are converted successfully.")
        print("* * * * * * * \n")


    def runImgFunc():
        funcImg2Pdf(fileList1)
        time.sleep(1)
        windowImg2PDF.destroy()


    # # # # # #   U I  O N L Y   # # # # #

    canvas1 = Canvas(windowImg2PDF, bg='#3A7FF6', width=390, highlightthickness=0)
    canvas1.pack(side="left", fill="y")


    textTitle = Label(
        windowImg2PDF,
        text="Image to PDF Converter", 
        bg="#3A7FF6", 
        fg="white", 
        justify="left", 
        font='menlo 20 bold'
        )
    textTitle.place(x=30, y=140)


    textStart = Label(
        windowImg2PDF,
        text="To get started, use the \nCHOOSE button and select image \nfile then click on CONVERT \nbutton to convert them into PDF.", 
        bg="#3A7FF6", 
        fg="white", 
        justify="left", 
        font='monaco 16'
        )
    textStart.place(x=30, y=200)


    textTip = Label(
        windowImg2PDF,
        text="Tip: You can choose multiple \nfiles to convert and merge all \nof them in one PDF file.", 
        bg="#3A7FF6", 
        fg="white", 
        justify="left", 
        font='menlo 16'
        )
    textTip.place(x=30, y=310) #290


    textWarning = Label(
        windowImg2PDF,
        text="Please choose .jpg, .jpeg, .png \nfiles only.", 
        bg="#3A7FF6", 
        fg="gold", 
        justify="left", 
        font='menlo 15'
        )
    textWarning.place(x=30, y=400)


    buttonOpen = Button(
        windowImg2PDF, 
        text="Choose File", 
        height=50, 
        width=150, 
        highlightbackground="white", 
        bg="#2979FF", 
        fg="white", 
        font="menlo 15",
        command=openImgFile
        )
    buttonOpen.place(x=460, y=140)


    buttonStart = Button(
        windowImg2PDF, 
        text="Convert", 
        height=50, 
        width=150, 
        highlightbackground="white", 
        bg="#00C853", 
        fg="white", 
        font="menlo 16",
        command=runImgFunc
        )
    buttonStart.place(x=650, y=140)


    textLastFile = Label(
        windowImg2PDF, 
        text="Last file selected: ",
        font='monaco 12',
        bg="white",
        fg="grey"
        )
    textLastFile.place(x=460, y=250)

    textFile = Label(
        windowImg2PDF, 
        textvariable=nameOfLast,
        font='monaco 12',
        bg="white",
        fg="grey"
        )
    textFile.place(x=600, y=250)


    textOut = Label(
        windowImg2PDF, 
        text="Output file name: ",
        font='monaco 12',
        bg="white",
        fg="grey"
        )
    textOut.place(x=460, y=300)

    textOutFile = Label(
        windowImg2PDF, 
        text=outputFileName,
        font='monaco 12',
        bg="white",
        fg="grey"
        )
    textOutFile.place(x=590, y=300)

    windowImg2PDF.mainloop()




# Getting date & time
current_time = datetime.datetime.now()
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute
outputFileName = f"{year}-{month}-{day}-{hour}.{minute}-merged.pdf"


# # # #  M A I N  code from here  # # # # 
homeWin = tkinter.Tk()
homeWin.geometry("838x556")
homeWin.minsize(579, 526)
homeWin.title("Home | PDF Operator")

# frame - 1
frame1 = Frame(homeWin, borderwidth=5, highlightbackground="grey", highlightcolor="grey", highlightthickness=1)
frame1.pack(side="top", padx=10, pady=40)

textWelcome = Label(frame1, text="Welcome to PDF Operator", padx=20, pady=13, font='helvetica 20 bold')
textWelcome.grid(row=0, column=0)


# frame - 2
frame2 = Frame(homeWin)
frame2.pack(side="top", padx=10, pady=10)

textConvert = Label(frame2, text="Convert your", font='Courier 35')
textConvert.config(foreground="light green")
textConvert.grid(row=0, column=0)

textfile = Label(frame2, text=" file easily!", font='Courier 35 bold')
textfile.config(foreground="cyan")
textfile.grid(row=0, column=1)


# frame - 3
frame3 = Frame(homeWin, borderwidth=3, highlightbackground="white", highlightcolor="white", highlightthickness=1)
frame3.pack(side="top", padx=10, pady=40)

textChoose = Label(frame3, text="Please choose the feature you want to use:", font='menlo 20', padx=20, pady=13)
textChoose.grid(row=0, column=0)

buttonMerge = Button(frame3, text="PDF Merger", height=40, width=130, command=windowMerge)
buttonMerge.grid(row=1, padx=10, pady=10)

buttonImgToPdf = Button(frame3, text="Image to PDF", height=40, width=130, command=Img2PdfFUNC)
buttonImgToPdf.grid(row=2, pady=20)


homeWin.mainloop()


# extractText()

# mergerPDF()


