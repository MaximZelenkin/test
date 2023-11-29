import os
import re
from PyPDF2 import PdfReader
import PyPDF2


file_list = re.findall(r'\w{1,30}\.pdf', str(os.listdir()))
merger = PyPDF2.PdfMerger()

print(file_list)

for pdf in file_list:
    try:
        #if doc exist then merge
        if True:
            input_1 = PdfReader(open(pdf, 'rb'))
            merger.append((input_1))
        else:
            print(f"problem with file {pdf}")

    except:
            print("cant merge !! sorry")
    else:
            print(f" {pdf} Merged !!! ")

merger.write("File_res.pdf")