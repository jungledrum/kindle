import os

from django.template import Template, Context
from django.conf import settings
from bs4 import BeautifulSoup


settings.configure()

path = "/home/bo/test/crawl_blog/books"
# path = "/home/bo/lab/a/test/book"

def get_articles():
    """
    path -> [title]
    """
    files = os.listdir(path)
    res = []
    for item in files:
        dot = item.rindex(".")
        filename, suffix = item[:dot], item[dot+1:]
        if suffix == "html":
            res.append(filename)
    return res


def create_opf(articles):
    with open("opf.tpl", "r") as f:
        content = f.read()
    t = Template(content)
    context = Context({"articles": articles})
    content = t.render(context)

    with open(path+"/blog.opf", "w") as f:
        f.write(content.encode("utf8"))


def create_toc(articles):
    with open("toc.tpl", "r") as f:
        content = f.read()
    t = Template(content)
    context = Context({"articles": articles})
    content = t.render(context)

    with open(path+"/toc.html", "w") as f:
        f.write(content.encode("utf8"))


def change_encode():
    files = get_articles()
    for item in files:
        with open(path+"/"+item+".html", "r") as f:
            html = f.read()
            soup = BeautifulSoup(html)
            s = """
            <head>
            <meta http-equiv="content-type" content="text/html; charset=utf-8">
            <meta charset="UTF-8">
            </head>
            """
            tag_head = soup.new_tag("head")
            tag_meta = soup.new_tag("meta")
            tag_meta["http-equiv"] = "content-type"
            tag_meta["content"] = "text/html; charset=utf-8"
            soup.html.body.insert_before(tag_head)
            soup.html.head.append(tag_meta)
        with open(path+"/"+item+".html", "w") as f:
            f.write(soup.__repr__())


def main():
    articles = get_articles()
    create_opf(articles)
    create_toc(articles)

# change_encode()
main()