from bs4 import BeautifulSoup
import requests
from broth import Page
from downloader import download
from pdf import makepdf

codeS = input("Enter sauce string:\t")

for code in codeS.split(';'):
    code = int(code)
    link = lambda sauce: "https://nhentai.to/g/"+str(sauce)

    home = Page(link(code))

    # Phase 1, gather information
    # Note: I can just save these informations as a pack for later use, lol
    # Note: Maybe even make a scraper for this and this alone lol

    # Meta Data
    # main div, id=info
    # info > h1 = Title ; info > h2 = Foreign TItle ; info > section = Tags;
    # 

    metaInfo = home.find_id('info')[0]
    sectionTags = [i for i in metaInfo.find('section') if i != "\n"] # the tricky part


    # print(metaInfo.find('h2').text) # doesn't work
    # Parodies, Chars, Tags, Artists, Groups, Languages, Categories
    
    mainTitle = metaInfo.find('h1').text

    metaDict = {
        "Title": mainTitle
    }

    for i in sectionTags:
        text = i.text.strip().replace("\n\n",":").replace("\n",",")
        key = text.split(":")[0] or text
        if text.split(":").__len__() > 1:
            value = text.split(":")[1]
        else:
            value = ""
        metaDict[key] = value

    print(metaDict)

    # Photo Data
    homeLastPhoto = home.find_class('gallerythumb', tag='a')[-1]
    saucePhotoCount = int(homeLastPhoto['href'].split('/')[-2])
    sauceImageHTML = homeLastPhoto.findChildren('img')[-1]
    imageWidth, imageHeight = sauceImageHTML['width'], sauceImageHTML['width']
    sauceImageCode = int(sauceImageHTML['src'].split('/')[-2])
    metaDict['Pages'] = str(saucePhotoCount)

    print("Sauce Gallery Code\t"+str(sauceImageCode))
    print("Sauce Page Numbers\t"+str(saucePhotoCount))

    # Phase 2, recurse and download

    galleryBaseLink = lambda code,count: f"https://t.dogehls.xyz/galleries/{str(code)}/{str(count)}.jpg"

    for photoInstance in range(1, saucePhotoCount+1):
        download(code, photoInstance, sauceImageCode, 1)

    makepdf(code, metaDict)