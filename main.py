import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from readability.readability import Document

db = MongoClient().crawler

def get_article_links():
    blog_links = [("http://www.geekonomics10000.com/page/"+str(x)) for x in range(1,31)]
    article_links = []
    for blog_link in blog_links:
        html = requests.get(blog_link)
        soup = BeautifulSoup(html.text)
        titles = soup.find_all("h3", class_="post-title")
        for title in titles:
            item = (title.a["href"], title.a.text)
            print item[0], item[1]
            article_links.append(item)

    return article_links

def save_links(links):
    for (link, title) in links:
        db.links.insert({
            "link": link,
            "title": title
        })

def crawl_article_html():
    links = db.links.find()
    for item in links:
        link = item.get("link", "")
        title = item.get("title", "")

        html = requests.get(link)
        db.articles.insert({
            "link": link,
            "html": html.text,
            "title": title
        })
        print link, title


def extract_article_text():
    articles = db.articles.find()
    for item in articles:
        id = item.get("_id", "")
        html = item.get("html", "")
        text = Document(html).summary()

        db.articles.update({"_id": id}, {"$set":{"text": text}})

def make_kinde_book():
    articles = db.articles.find()
    for item in articles:
        title = item.get("title", "")
        text = item.get("text", "")

        print title
        with open("./books/"+title+".html", "w") as f:
            f.write(text.encode("utf8"))



def main():
    links = get_article_links()
    for (link, title) in links:
        article = extract_article(link)
        save_article(article)

make_kinde_book()