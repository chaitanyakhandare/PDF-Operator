Here’s a basic structure for your README file:

---

# PDF Operator 📝

Welcome to **PDF Operator**, a Python-based tool that helps you manage and manipulate PDF files. This tool provides several handy features, including PDF text extraction, PDF merging, splitting PDF pages, and converting images to PDFs. 

## Features 🚀

1. **PDF Text Extractor**  
   Extract text from a specific page of a PDF document and store it in a text file.

2. **PDF Merger**  
   Merge multiple PDF files into one, creating a new merged PDF document.

3. **Image to PDF Converter**  
   Convert one or multiple images (JPEG, PNG) into a PDF file and merge them.

4. **PDF Splitter**  
   Split specific pages from a PDF document into a new file.

## Requirements 🛠️

Before you begin, ensure you have met the following requirements:

- Python 3.x
- PyPDF2
- img2pdf

You can install the dependencies using:

```bash
pip install PyPDF2 img2pdf
```

## Usage 💻

### 1. Extract Text from a PDF
Extracts text from a specific page and stores it in a `.txt` file.

```bash
Enter full path of your document: [path_to_pdf]
Enter page number to extract text: [page_number]
```

### 2. Merge PDF Files
Merge multiple PDF files into a single document.

```bash
Enter full paths of files to merge (to stop type: exit)
```

### 3. Convert Images to PDF
Convert images (JPEG/PNG) to a PDF.

```bash
Enter full paths of files to merge (to stop type: exit)
```

### 4. Split PDF Pages
Split specific pages from a PDF into a new document.

```bash
Enter path of PDF file
Enter page numbers to split (type 'done' to end)
```

### Example Paths
You can use the following examples to test the tool:

```bash
/Users/Documents/bill.pdf
/Users/Downloads/Screenshot.png
```
