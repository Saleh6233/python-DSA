import PyPDF2
# import sys
# with open("./218 - dummy.pdf", 'rb') as filePdf:
#     reader = PyPDF2.PdfReader(filePdf)
#     print(len(reader.pages))

# with open("./218 - dummy.pdf", 'rb') as filePdf:
#     reader = PyPDF2.PdfReader(filePdf)
#     print(reader.pages[0])

# Rotating a pdf and saving as different file
# with open("./218 - dummy.pdf", 'rb') as filePdf:
#     reader = PyPDF2.PdfReader(filePdf)
#     page = reader.pages[0]
#     page.rotate(90)

#     writerObj = PyPDF2.PdfWriter()
#     writerObj.add_page(page)

#     with open("./tilt.pdf", 'wb') as new_file:
#         writerObj.write(new_file)


# merging pdfs
# inputs = sys.argv[1:]  # It will take all inputs except 1st one


# def pdf_combiner(pdf_list):

#     merger = PyPDF2.PdfMerger()
#     i = 1
#     for pdf in pdf_list:
#         print(f"{i}. {pdf}")
#         merger.append(pdf)
#         i = i+1

#     merger.write("super.pdf")
#     merger.close()


# print("Showing all pdf list: ")
# pdf_combiner(inputs)


# Watermarking Pdf
content_pdf = PyPDF2.PdfReader(open("./super.pdf", 'rb'))

stamp_pdf = PyPDF2.PdfReader(open("./wtr.pdf", 'rb'))

output_pdf = PyPDF2.PdfWriter()

for i in range(len(content_pdf.pages)):
    page = content_pdf.pages[i]
    page.merge_page(stamp_pdf.pages[0])
    output_pdf.add_page(page)

    with open("watermarked.pdf", 'wb') as new_file:
        output_pdf.write(new_file)
