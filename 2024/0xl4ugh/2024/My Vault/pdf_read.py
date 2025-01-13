from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_file):
	reader = PdfReader(pdf_file)
	text = ""
	for page in reader.pages:
		text += page.extract_text() + "\n"
	return text


# totally didn't get from chat gipity
# only correct for single word country name
if __name__ == "__main__":
	pdf_file = "countries2.pdf"  # Replace with your PDF file name
	extracted_text = extract_text_from_pdf(pdf_file)
	file = open('countries2.txt', 'w')
	for line in extracted_text.splitlines():
		if line.split(' ')[0].isdigit():
			print(line.split(' ')[1].encode())
			file.write(line.split(' ')[1] + '\n')
	file.close()