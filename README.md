# PDF Operator

**PDF Operator** is a Python-based tool that provides multiple PDF functionalities, including merging, splitting, extracting text, and converting images to PDFs. It offers both a console-based version with more features and a GUI-based version for simpler, user-friendly interactions.

## Features

### 1. Console-Based Version (Advanced Features)
- **PDF Text Extractor**: Extract text from a specific page of a PDF document.
- **PDF Merger**: Merge multiple PDF files into one.
- **Split PDF Pages**: Split selected pages from a PDF document into a new file.
- **Image to PDF Converter**: Convert image files (JPG, PNG, etc.) into a PDF file (with merging capability).

### 2. GUI-Based Version (Simplified)
- **PDF Merger**: Merge multiple PDF files through a simple user interface.
- **Image to PDF Converter**: Convert and merge multiple images into a single PDF file.

---

## Getting Started

### Prerequisites
To run this project, you’ll need the following Python libraries:
- `PyPDF2`
- `img2pdf`
- `tkinter` (for the GUI version)
- `tkmacosx` (for better button styling in macOS)

You can install these libraries via pip:
```bash
pip install PyPDF2 img2pdf tkmacosx
```

---

## Console-Based Version

### How to Use

1. **Clone the repository** and navigate to the folder:
    ```bash
    https://github.com/chaitanyakhandare/PDF-Operator-withGUI.git
    cd PDF-Operator-withGUI
    ```

2. **Run the script**:
    ```bash
    python pdfOperator.py
    ```

3. **Select the feature** you want to use from the menu:
    - Press `1` for PDF Text Extractor.
    - Press `2` for PDF Merger.
    - Press `3` for Image to PDF conversion.
    - Press `4` for Split PDF Pages.
    - Press `99` to exit.

### Features Description

- **PDF Text Extractor**:
    - Enter the path to the PDF file and the page number to extract the text.
    - The extracted text will be saved to a file.

- **PDF Merger**:
    - Provide the paths of the PDF files to be merged, and the tool will create a new merged PDF.

- **Image to PDF**:
    - Convert multiple image files (JPG, PNG, etc.) into a single PDF file.

- **Split PDF Pages**:
    - Select specific pages from a PDF to split into a new file.

---

## GUI-Based Version

### How to Use

1. **Run the GUI-based script**:
    ```bash
    python pdf_operator_gui.py
    ```

2. **Choose your desired feature** from the user interface:
    - Click on `PDF Merger` to merge PDF files.
    - Click on `Image to PDF` to convert images into a single PDF.

### Features Description

- **PDF Merger**:
    - Use the `Open file` button to select multiple PDF files, and then click `Start Merging` to merge them into one PDF.

- **Image to PDF**:
    - Select multiple image files (JPG, JPEG, PNG) to convert and merge them into a PDF file by clicking the `Convert` button.

---
