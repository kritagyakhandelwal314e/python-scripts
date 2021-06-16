import PyPDF2

template = PyPDF2.PdfFileReader(open('PDF/merged_pdf.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('PDF/wtr.pdf', 'rb'))
watermark_page = watermark.getPage(0)
output = PyPDF2.PdfFileWriter()

for page_num in range(template.getNumPages()):
    page = template.getPage(page_num)
    page.mergePage(watermark_page)
    output.addPage(page)
    with open('PDF/watermarked.pdf', 'wb') as file:
        output.write(file)
