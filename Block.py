import feedparser as f
import lxml.html as html
import requests 
import urllib.request

class Lenta():
    
    link = "https://lenta.ru/rss"

    def news (self, num):

        d = f.parse(self.link)
        try:
            if d.bozo:
                raise d.bozo_exception
        finally:
            
            data = [{"title":d.entries[i].title, "link":d.entries[i].link,
                "desc":d.entries[i].description,
                "published":d.entries[i].published} for i in range(1,num+1)] 

            return data

    def grub (self, link, title = "None", img = "None", content = "None"):

        lentaContent = []
        page = requests.get(link)

        charset = urllib.request.urlopen(link).headers.get_content_charset()

        try:
            tree = html.fromstring(page.content.decode(charset))
        except:
            tree = html.fromstring(page.content.decode('windows-1251'))

        for div in tree.cssselect('div.b-text p'):
            lentaContent.append(div.text_content())
        lentaTitle = tree.cssselect('h1.b-topic__title')[0].text
        try:
            lentaImage = tree.cssselect('div.b-topic__title-image img.g-picture')[0].get("src")
        except:
            lentaImage = 'None'

        lentaArticle = {"title": lentaTitle,
                    "image": lentaImage,
                    "content": lentaContent}
        return lentaArticle

class Parser():
    
    def __init__(self, link):
        self.link = link
    
    def news (self, num):

        d = f.parse(self.link)
        try:
            if d.bozo:
                raise d.bozo_exception
        finally:
            
            data = [{"title":d.entries[i].title, "link":d.entries[i].link,
                "desc":d.entries[i].description,
                "published":d.entries[i].published} for i in range(1,num+1)] 

            return data
    
    def grub (self, link, title = "None", img = "None", cont = "None"):

        Content = []
        page = requests.get(link)

        charset = urllib.request.urlopen(link).headers.get_content_charset()

        try:
            tree = html.fromstring(page.content.decode(charset))
        except:
            tree = html.fromstring(page.content.decode('windows-1251'))

        if cont != "None":
            for div in tree.cssselect(cont):
                Content.append(div.text_content())
        else: Content.append(cont)    
        
        try:
            if img != "None":    
                Image = tree.cssselect(img)[0].get("src")
            else: Image = img 
        except:     
            Image = "None"  
        if title != "None":
            Title = tree.cssselect(title)[0].text
        else: Title = title 

        Article = {"title": Title,
                    "image": Image,
                    "content": Content}
        return Article