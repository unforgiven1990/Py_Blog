import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import os.path
from selenium import webdriver
from datetime import date
import time
import glob, os
import os
import openpyxl
import re
#import pinyin
from pypinyin import pinyin, lazy_pinyin, Style
import shutil
from PIL import Image

from pathlib import Path
from pandas.api.types import is_string_dtype
from bs4 import BeautifulSoup
from pypinyin import pinyin, lazy_pinyin, Style
"""
tp=template of a component
cp=instance of a component (a instance of template)
do tp and component as two layer of abstractions to get the granularity better
pg=page (many components together create a page)
template and cp can be modified to another need
create webpages with sinolino
fully modular
fully extendable, adjustable
"""

def replace_cn_name(name):
    for ch in [":", "?", ">", "<", "|", '"', "*", "/", "！", "·", "—", " "]:
        name = name.replace(ch, "")
    return name


def create_toc(content):
    #this toc is only used for mobile version, for desktop version the toc is sticky
    result=""
    content=BeautifulSoup(content)
    for counter, h2 in enumerate(content.select("h2")):
        result=result+f"<li class='nodot'><a href='#header_{counter+1}'>"+h2.text+"</a></li>"
    return "<ul class='mt-3 bg-light mobile_toc' >Summary: "+result+"</ul>"


def get(folder="template", item="h1.html", purpose=3):
    if purpose==1: #get path for python
        return f"{folder}/{item}"
    elif purpose==2: #get path for html rendering
        return f"../{folder}/{item}"
    elif purpose ==3: #get file content itself
        return open(f"{folder}/{item}", "r", encoding='utf-8').read()


def to_page(page,filename):
    Path(f"page").mkdir(parents=True, exist_ok=True)
    with open(fr"page/{filename}.html", "w", encoding="utf-8") as file:
        file.write(str(page))

def get_all_images(CN_name):
    try:
        clean_en_name = replace_cn_name(replace_cn_name(CN_name))
        cn_name_pinyin = "-".join(lazy_pinyin(clean_en_name))
    except Exception as e:
        return

    root_path_en = f"Douban/Show/upload"
    shopify_url = "https://cdn.shopifycdn.net/s/files/1/0687/0145/4658/files/"
    a_imgs=[]
    for (root, dirs, files) in os.walk(root_path_en, topdown=True):
        for file in files:
            if cn_name_pinyin in file:
                shutil.copyfile(f"Douban/Show/upload/{file}", f"img/{clean_en_name}.webp")
                clean_en_name = replace_cn_name(file)
                tag = get(item="img.html").format(src=f"../img/{clean_en_name}.webp")
                a_imgs+=[tag]
    return "".join(a_imgs)


def create_blog_page(blog,article_url, article_title):
    nav_element=get(folder="template",item="nav_element.html",purpose=3).format(icon='',name='blog', href="../page/index.html")
    nav = get(folder="template", item="nav.html", purpose=3).format(elements=nav_element)
    body_container=get(folder="template", item="body_container_blog.html", purpose=3)
    speechify_js=get(folder="asset", item="speechify.js", purpose=2)
    speechify_js=f"<script src='{speechify_js}'></script>"
    page = get(folder="template", item="page.html", purpose=3).format(title=title.replace("-"," "),head="",body=nav+body_container+speechify_js)
    return page


def create_index_page(blog):
    nav_element=get(folder="template",item="nav_element.html",purpose=3).format(icon='',name='blog', href="../page/index.html")
    nav = get(folder="template", item="nav.html", purpose=3).format(elements=nav_element)
    body_container=get(folder="template", item="body_container_index.html", purpose=3)

    page = get(folder="template", item="page.html", purpose=3).format(title=blog,head="",body=nav+body_container)
    return page


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)


def cut_summary(summary, maxlen=150):
    if len(summary) < maxlen:
        return summary

    traversed_chars=''
    for char in summary:
        traversed_chars+=char
        break_loop=True if len(traversed_chars) > maxlen else False
        if break_loop and char==" ":
            return traversed_chars +"..."
    return traversed_chars +" ..." # should stop but didnt found any whitespace to stop

def get_lis(url,row):
    dict_base = ["EN Name", "Summary"]
    dict_video = ["Youtube", "MangoTV", "iQiyi", "Tencent", "Youku", "Bilibili", "Ole", "Other"]
    dict_article = ["IMDB", "Douban", "Weibo", "CN Wikipedia", "Baidu"]
    dict_display = ["Alt Name", "Rating", "Genre", "First EP", "Season", "EP", "Actors"]

    lis=[]
    for label in dict_video+ dict_article:
        if not pd.isna(row[label]):
            a=f"<li>Link: <a href='{row[label]}' target='_blank'>{label}</a></li>"
            lis+=[a]

    for label in dict_display:
        if not pd.isna(row[label]):
            if label=="Actors":
                a=f"<li>{label}: {row['EN Actors']} ({row[label]})</li>"
            elif label=="EP":
                a=f"<li>{label}: {int(row[label])}</li>"
            else:
                a=f"<li>{label}: {row[label]}</li>"
            lis+=[a]

    return ''.join(lis)

def get_article(url):
    #generate articles to put it into douban
    df= pd.read_excel("Douban/step4.xlsx").set_index("url", drop=True)
    column_name=f"A_{url}"

    if not column_name in df.columns:
        print(url, " not in df, skip")
        return ""

    df=df[df[column_name].notna()].sort_values(by=column_name)

    content=[]
    for counter, (url, row) in enumerate(df.iterrows()):
        spy_title = f"{counter+1}. " + row["EN Name"].split("Season")[0]
        title=f"{counter+1}. {row['EN Name']}({row['CN Name']})"
        title_id=f"header_{counter+1}"
        summary=row["Summary"]
        lis=get_lis(url,row)

        if pd.isna(row["Youtube"]):
            youtube = ""
        else:
            youtube_id = row["Youtube"].split("watch?v=")[1].split("&")[0]
            youtube=get(item="youtube_iframe.html").format(youtube_title=title,src=f"https://www.youtube.com/embed/{youtube_id}")

        imgs=get_all_images(row["CN Name"])
        blog_item=get(item="blog_item.html").format(spy_title=spy_title, title=title,summary=summary, lis=lis, youtube=youtube,imgs=imgs, title_id=title_id)
        content+=[blog_item]
    return "".join(content)


if __name__ == '__main__':
    for blog in ["Sinolino"]: #reserve place for future multiple website

        """build index pages"""
        data = pd.read_excel("Douban/external/data.xlsx")
        footer = f"{blog} @ {date.today().year}"
        row_on_index=3

        #create all items
        blog_articles=[]
        for title, url, published,summary in zip(data["title"], data["url"], data["published"],data["summary"]):
            summary=cut_summary(summary)
            img = get("Douban/external", item=url+".webp", purpose=2)
            a_title=f"<a href='{get(folder='page',item=url+'.html',purpose=2)}'>"+title+"</a>"
            blog_short=get("template",item="blog_short.html",purpose=3)
            blog_articles+=[blog_short.format(title=a_title,published=published, summary=summary, img=img)]


        #fill the list until 3x elements so the list can be used for next function
        blog_articles += [""]* (row_on_index-( len(blog_articles) % row_on_index))

        columns = []
        for list_of_items in grouped(blog_articles, row_on_index):
            list_with_col=[f'<div class="col">{x}</div>' for x in list_of_items]
            column = get(item="row_0.html").format("".join(list_with_col))
            columns += [column]

        frame = create_index_page(blog=blog).format(h1=blog,  content="".join(columns),footer=footer)
        to_page(page=frame, filename="index")


        """build blog pages"""
        for title, url, published,summary in zip(data["title"], data["url"], data["published"],data["summary"]):
            content = get_article(url)
            toc=create_toc(content)
            img = get("img/feature", item=url + ".webp", purpose=2)
            frame = create_blog_page(blog=blog, article_url=url,article_title=title).format(h1=title, time=published, img=img, toc=toc, summary=summary, content=content,footer=footer)
            to_page(page=frame, filename=url)

        """about page, 404 page, other pages"""



