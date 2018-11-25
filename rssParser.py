import feedparser as f
import lxml.html as html
import requests 

#Parse lenta

d = f.parse('https://lenta.ru/rss')
if d.bozo:
    raise d.bozo_exception

lentaNews = [{"title":d.entries[i].title, "link":d.entries[i].link,
            "desc":d.entries[i].description,
            "published":d.entries[i].published} for i in range(1)]
print (lentaNews)

lentaContent = []
page = requests.get(lentaNews[0]["link"])
tree = html.fromstring(page.content.decode('utf-8'))
for div in tree.cssselect('div.b-text p'):
    lentaContent.append(div.text_content())
lentaTitle = tree.cssselect('h1.b-topic__title')[0].text
lentaImage = tree.cssselect('div.b-topic__title-image img.g-picture')[0].get("src")

lentaArticle = {"title": lentaTitle,
            "image": lentaImage,
            "content": lentaContent}
print(lentaArticle)
print("")

#Parse interfax

d = f.parse('https://www.interfax.ru/rss.asp')
if d.bozo:
    raise d.bozo_exception

interfaxNews = [{"title":d.entries[i].title, "link":d.entries[i].link,
            "desc":d.entries[i].description,
            "published":d.entries[i].published} for i in range(1)]
print (interfaxNews)

interfaxContent = []
page = requests.get(interfaxNews[0]["link"])
tree = html.fromstring(page.content)
for div in tree.cssselect('div.at p'):
    interfaxContent.append(div.text_content())
interfaxTitle = tree.cssselect('h1.textMTitle')[0].text
interfaxImage = "None"

interfaxArticle = {"title": interfaxTitle,
            "image": interfaxImage,
            "content": interfaxContent}
print(interfaxArticle)
print("")

#parse kommersant

d = f.parse('http://www.kommersant.ru/RSS/news.xml')
if d.bozo:
    raise d.bozo_exception

kommersantNews = [{"title":d.entries[i].title, "link":d.entries[i].link,
            "desc":d.entries[i].description,
            "published":d.entries[i].published} for i in range(1)]
print (kommersantNews)

kommersantContent = []
page = requests.get(kommersantNews[0]["link"])

tree = html.fromstring(page.content.decode('windows-1251'))
for div in tree.cssselect('div.article_text_wrapper p'):
    kommersantContent.append(div.text_content())

kommersantTitle = tree.cssselect('h1.article_name')[0].text
kommersantImage = "None"

kommersantArticle = {"title": kommersantTitle,
            "image": kommersantImage,
            "content": kommersantContent}
print(kommersantArticle)
print("")

#parse m24

d = f.parse('https://www.m24.ru/rss.xml')

m24News = [{"title":d.entries[i].title, "link":d.entries[i].link,
            "desc":d.entries[i].description,
            "published":d.entries[i].published} for i in range(1)]
print (m24News)

m24Content = []
page = requests.get(m24News[0]["link"])

tree = html.fromstring(page.content.decode('UTF-8'))
for div in tree.cssselect('div.js-mediator-article p'):
    m24Content.append(div.text_content())
del m24Content[0]
del m24Content[-1]
m24Title = tree.cssselect('div.b-material-before-body__data h1')[0].text
m24Image = tree.cssselect('div.b-material-incut-m-image img')[0].get("src")

m24Article = {"title": m24Title,
            "image": m24Image,
            "content": m24Content}
print(m24Article)
print("")