import PyPDF2
templet=PyPDF2.PdfFileReader(open('Super.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
writer=PyPDF2.PdfFileWriter()
for i in range(templet.getNumPages()):
    pages=templet.getPage(i)
    pages.mergePage(watermark.getPage(0))
    writer.addPage(pages)
with open('Merged.pdf','wb') as file:
    writer.write(file)