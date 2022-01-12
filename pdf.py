import pprint
from os import listdir
from PIL import Image
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict


def makepdf(sauce, metadata):
    imglist = []
    for imageCount in listdir(str(sauce)):
        print(imageCount + " added into the pdf")
        path = f"{str(sauce)}/{imageCount}"
        try:
            imglist.append(Image.open(path).convert("RGB"))
        except Exception:
            print(f"Page {imageCount} wasn't found or corrupted")
    img0 = imglist[0]
    img0.save(f"{sauce}.pdf", save_all=True, append_images=imglist[1:])
    addMeta(f"{sauce}.pdf", metadata)


def addMeta(filename, meta):
    # TODO: comment this line soon
    print("Writing PDF metadata")
    # pdf_reader = PdfReader(filename)
    # metadata = PdfDict(meta)
    # pdf_reader.Info.update(metadata)
    # PdfWriter().write(f'0{filename}', pdf_reader)
    # file_in = open(filename, "rb")
    # pdf_reader = PdfFileReader(file_in)
    # metadata = pdf_reader.getDocumentInfo()
    # pprint.pprint(metadata)

    # pdf_writer = PdfFileWriter()
    # pdf_writer.appendPagesFromReader(pdf_reader)
    # pdf_writer.addMetadata(meta)
    # file_in.close()
    # file_out = open(f"{filename}", "wb")
    # pdf_writer.write(file_out)
    # file_out.close()


    # inputs = sys.argv[1:]
    # assert inputs
    # outfn = "cat." + os.path.basename(inputs[0])

    writer = PdfWriter(f'X{filename}')
    writer.addpages(PdfReader(f'{filename}').pages)

    writer.trailer.Info = IndirectPdfDict(
        Title=meta['Title'],
        Keywords=meta['Tags'],
        Author=meta['Artists'],
        Subject=meta['Groups']
    )
    writer.write()

# def makepdf(sauce):
#     pdf = FPDF()
#     # imagelist is the list with all image filenames
#     for imageCount in listdir(str(sauce)):
#         imagePath = f'{sauce}/{imageCount}'
#         width, height = imageSize(imagePath)
#         pdf.add_page()
#         pdf.image(imagePath,0,0,300,300)
#     pdf.output(f"{str(sauce)}.pdf", "F")

# def imageSize(path):
#     img = PIL.Image.open(path)
#     return img.size

if __name__ == "__main__":
    makepdf(374304)
