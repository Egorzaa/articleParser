from Block import Parser, Lenta

lenta = Lenta()
news = lenta.news(1)
print(news)

url = news[0]['link']
data = lenta.grub(url)
print(data)


# Create new rss parser for Lenta

parse = Parser("https://lenta.ru/rss")  #get rss website data by link
news = parse.news(1)   # number - news quantity to get
print(news)

url = news[0]['link']  # get article by news number (starts from 0)

# enter where to find data on site
data = parse.grub(url, cont = 'div.b-text p', 
                    img = 'div.b-topic__title-image img.g-picture', title = 'h1.b-topic__title')
print(data)



# Create new rss parser for Interfax

parse = Parser("https://www.interfax.ru/rss.asp")  
news = parse.news(1)   
print(news)

url = news[0]['link']  
data = parse.grub(url, cont = 'div.at p', 
                        title = 'h1.textMTitle')
print(data)



# Create new rss parser for Kommersant

parse = Parser("http://www.kommersant.ru/RSS/news.xml")  
news = parse.news(1)  
print(news)

url = news[0]['link']  
data = parse.grub(url, cont = 'div.article_text_wrapper p', 
                        title = 'h1.article_name')
print(data)



# Create new rss parser for m24

parse = Parser("https://www.m24.ru/rss.xml") 
news = parse.news(1)  
print(news)

url = news[0]['link'] 

data = parse.grub(url, cont = 'div.js-mediator-article p', 
                        img = 'div.b-material-incut-m-image img',
                        title = 'div.b-material-before-body__data h1')
print(data)



# Create new rss parser for life

parse = Parser("https://life.ru/xml/feed.xml") 
news = parse.news(1)  
print(news)

url = news[0]['link'] 

data = parse.grub(url, cont = 'div.content-note p', 
                        img = 'figure.post-page-image img',
                        title = 'header.post-page-header h1')
print(data)