import PyPDF2

def pdf_parser(file_path):
    """
    Extract text from a PDF file.
    """
    pdf_file = open(file_path, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    text = ''
    for page_number in range(number_of_pages):
        page = read_pdf.getPage(page_number)
        page_content = page.extractText()
        text += page_content
    pdf_file.close()
    return text

def main():
    file_path = input("Enter the PDF file path: ")
    text = pdf_parser(file_path)
    print("Extracted text:")
    print(text)

if __name__ == "__main__":
    main()