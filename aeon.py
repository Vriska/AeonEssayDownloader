import requests
from bs4 import BeautifulSoup
import re

class Aeon :
    def __init__(self):
        self.Title = " "
        self.Intro = " "
        self.Paragraphs = []

    def data(self,URL):                                     #Gets title ,heading from an essay
        r = requests.get(URL)
        Soup = BeautifulSoup(r.content,"html.parser")
        self.Title = Soup.find('h1').get_text()
        self.Intro = Soup.find('h2').get_text()
        self.Paragraphs = Soup.find_all('p')


    def wordwrite(self):                                     # Creates text file
        p = re.compile("\\n|\?|\W(?!\S)",flags=re.U)
        filename = (p.sub("",self.Title,count=10))
        file = open("C:\\Users\Anirudh\Desktop\BJ\\"+str(filename)+".txt","a+")
        file.write(filename)
        file.write(self.Intro)
        for text in self.Paragraphs[1:len(self.Paragraphs)-13] :             # Rids of bogus lines at the bottom 
            try :
                file.write(text.get_text()+"\n")
                file.write("\n")
                print(text.get_text())
            except :
                file.write('Filewritefailure')
                print("spec")
        file.close()

    def Lcreate(number=1):   # Creates a list of aeon essays
        PageNumber = number  # Star scraping from first page of aeon essay
        r = requests.get('https://aeon.co/essays?page=' + str(PageNumber))
        Soup = BeautifulSoup(r.content, "html.parser")
        L = [link.get('href') for link in Soup.find_all('a')]
        L.append('PENUS')
        L[:] = [ele for ele in L if re.match("^/essay", ele) is not None]
        return list(map(lambda x: 'http://www.aeon.co' + x, L))


a = Aeon()
for x in range(32,33):
    for URL in a.Lcreate(x) :
        a.data(URL)
        a.wordwrite()
