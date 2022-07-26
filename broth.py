from requests import get
from bs4 import BeautifulSoup

class Page:
    """
    _version 0.1_
    Boilerplate code for bs4-requests web scraping summarized into a class
    very outdates, shouldn't have used it as a class, but a function
    """
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    parser = 'html.parser'
    def __init__(self, url):
        self.url = url
        self.req = get(url, headers=self.headers)
        self.soup = BeautifulSoup(self.req.content, self.parser)
    def find_class(self, class_name, tag='div'):
        return [i for i in self.soup.find_all(tag, attrs={"class": class_name})]
    def find_id(self, id_name, tag='div'):
        return [i for i in self.soup.find_all(tag, attrs={"id": id_name})]
    def find(self, attrs:dict, tag='div'):
        return self.soup.find(tag, attrs=attrs)