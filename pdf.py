from os import listdir
from PIL import Image

def makepdf(sauce):
    imglist = []
    for imageCount in listdir(str(sauce)):
        print(imageCount + " added into the pdf")
        path = f"{str(sauce)}/{imageCount}"
        try:
            imglist.append(Image.open(path).convert('RGB'))
        except Exception:
            print(f"Page {imageCount} wasn't found or corrupted")
    img0 = imglist[0]
    img0.save(f'{sauce}.pdf',save_all=True, append_images=imglist[1:])

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

if __name__=="__main__":
    makepdf(374304)