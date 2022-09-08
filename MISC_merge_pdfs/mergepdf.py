from PyPDF2 import PdfFileMerger

pdfs = ['SEABORN1.pdf', 'SEABORN2.pdf', 'SEABORN3.pdf', 'SEABORN4.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()

