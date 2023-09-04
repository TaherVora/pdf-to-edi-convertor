import PyPDF2

# Function to extract text from a PDF file
def extract_pdf_text(pdf_file_path):
    text = ""
    try:
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
    return text

# Function to map PDF data to EDI format (sample mapping)
def map_pdf_to_edi(pdf_text):

    edi_data = "PDF_TEXT: " + pdf_text + "\n"

    return edi_data

# Main function to convert PDF to EDI
def mainly(pdf_file_path,edi_file_path):
    pdf_text = extract_pdf_text(pdf_file_path)
    edi_data = map_pdf_to_edi(pdf_text)
    #--Khali print krvo hoi data to return vadi line uncomment kri deje and Save vadi 2 line comment kri deje
    # return edi_data
    # Save the EDI data to a file
    with open(edi_file_path, 'w') as edi_file:
        edi_file.write(edi_data)

if __name__ == "__main__":
    pdf_file_path = "/Users/tahervora/Downloads/fritolay.pdf"  # Replace with the path to your PDF file
    edi_file_path = "/Users/tahervora/Downloads/output.edi"  # Replace the path for the output EDI file
    edi_result = mainly(pdf_file_path,edi_file_path)
    print("File saved")
    # Print or save the EDI data as needed
    # print("Converted EDI Data:")
    # print(edi_result)

