from bs4 import BeautifulSoup
import requests
from broth import Page
from downloader import download
from pdf import makepdf

code = int(input("Enter sauce:\t"))

link = lambda sauce: "https://nhentai.to/g/"+str(sauce)

home = Page(link(code))

# Phase 1, gather information
# Note: I can just save these informations as a pack for later use, lol
# Note: Maybe even make a scraper for this and this alone lol

homeLastPhoto = home.find_class('gallerythumb', tag='a')[-1]
saucePhotoCount = int(homeLastPhoto['href'].split('/')[-2])
sauceImageHTML = homeLastPhoto.findChildren('img')[-1]
imageWidth, imageHeight = sauceImageHTML['width'], sauceImageHTML['width']
sauceImageCode = int(sauceImageHTML['src'].split('/')[-2])

print(sauceImageCode, saucePhotoCount)

# Phase 2, recurse and download

galleryBaseLink = lambda code,count: f"https://t.dogehls.xyz/galleries/{str(code)}/{str(count)}.jpg"

for photoInstance in range(1, saucePhotoCount+1):
    download(code, photoInstance, sauceImageCode, 1)

makepdf(code)