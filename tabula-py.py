from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter

fp = open('Example.pdf', 'rb')
outfp = open('Example.txt', 'wb')
rsrc = PDFResourceManager()
device =TextConverter(rsrc, outfp)

process_pdf(rsrc, device, fp, maxpages=2)

fp.close()
outfp.close()