import PyPDF2
import sys
pdffile=sys.argv[1:]
def pdf_Merger(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for i in pdf_list:
        merger.append(i)
    merger.write('Super.pdf')
pdf_Merger(pdffile)
