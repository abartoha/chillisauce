import pprint
from os import listdir, remove
from PIL import Image
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict


def makepdf(sauce, metadata):
    imglist = []
    sorted_list_dir = listdir(str(sauce)) 
    sorted_list_dir.sort()
    # adding this after testing this on arch linus
    # apparantly arch linux returns 00-7.jpg first, 
    # then 0015.jpg I don't know why tf
    for imageCount in sorted_list_dir:
        print(imageCount + " added into the pdf")
        path = f"{str(sauce)}/{imageCount}"
        try:
            imglist.append(Image.open(path).convert("RGB"))
        except Exception:
            print(f"Page {imageCount} wasn't found or corrupted")
    if imglist == []:
        return -1
    img0 = imglist[0]
    img0.save(f"{sauce}.pdf", save_all=True, append_images=imglist[1:])
    addMeta(f"{sauce}.pdf", metadata)
    remove(f"{sauce}.pdf")
    return 0


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

    writer = PdfWriter(fileNameWindows(meta['Title'])+".pdf")
    writer.addpages(PdfReader(f'{filename}').pages)

    writer.trailer.Info = IndirectPdfDict(
        Title=meta['Title'],
        Keywords=meta['Tags'],
        Author=meta['Artists'],
        Subject=meta['Groups']
    )
    writer.write()

def fileNameWindows(name, r=" x "):
    # WARNING: this might cause unexpected behavior
    # this fuction makes a string compatible with the file naing scheme of windows perating system
    new_name = ""
    for i in name:
        if i in "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 [ ] ( ) ! . , - + _".split(" "):
            new_name += i
    return new_name

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
    
    
