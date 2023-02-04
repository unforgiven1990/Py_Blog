import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import os.path
from selenium import webdriver
from distutils.dir_util import copy_tree
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
from string import Formatter
import mammoth
from pathlib import Path
from pandas.api.types import is_string_dtype
from bs4 import BeautifulSoup
import pathlib
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




def create_toc(content):
    #this toc is only used for mobile version, for desktop version the toc is sticky
    result=""
    content=BeautifulSoup(content, "html.parser")
    for counter, h2 in enumerate(content.select("h2")):
        result=result+f"<li class='nodot'><a href='#header_{counter+1}'>"+h2.text+"</a></li>"
    return "<ul class='mt-3 bg-light mobile_toc' >Summary: "+result+"</ul>"


def get(path="h1.html", way=3):
    if way==1: #get path for python
        return f"{path}"
    elif way==2: #get path for html rendering like img path
        return f"../{path}"
    elif way ==3: #get file content itself
        return open(f"{path}", "r", encoding='utf-8').read()

def get_template(name,way=3):
    """get html template like h1.html"""
    if ".html" in  name:
        return get(path=f"template/{name}", way=way)
    else:
        return get(path=f"template/{name}.html", way=way)

def get_content(blog_url, file, way=3):
    """get content like how tocebome project manager.html"""
    if ".html" in  file:
        return get(path=f"{blog_url}/{file}", way=way)
    else:
        return get(path=f"{blog_url}/{file}.html", way=way)


def get_d_template(way=3):
    """returns all template as dict
    way 1. key = page.html, val =html content
    way 2. key = page, val =html content
    way 3. key = $page, val =html content
    """
    d_template={}
    a_template=get_files(path="template",ending=".html")
    for template in a_template:
        d_way={
            1:template,
            2:template.replace(".html",""),
            3:"$"+template.replace(".html",""),
        }
        d_template[d_way[way]]=get_template(template)
    return d_template




def output_file(page, filename, pname):
    with open(fr"{filename}", "w", encoding="utf-8") as file:
        file.write(str(page))


def resolve(template):
    """resolves a template and fits all his modules"""
    a_replaced=[]
    d_template=get_d_template(way=3)
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if "$" in var  and var in d_template.keys():
            print(f"{var} in can be replaced")
            a_replaced+=[var]
        else:
            d_template[var]="{"+var+"}"
    template = template.format(**d_template)

    return resolve(template) if len(a_replaced) >0 else template



def content_h2list(content):
    """
    add a list to all h2 titles
    """
    soup = BeautifulSoup(content, 'html.parser')
    for counter, h2 in enumerate(soup.find_all(name="h2")):
        h2.string=f"{counter+1}. {h2.string}"
    return str(soup)

def content_scrollspy(content):
    """
    1. the generated html file is not directly scrollspyable
    2. convert <h2><p> to <section><h2><p></section>
    """
    soup=BeautifulSoup(content,'html.parser')
    new_content=""
    current_section=""
    current_title=""
    for child in soup.findChildren():
        if child.name=="h2" or current_section:#open section by h2 or still opened
            current_section+=str(child)
        else:
            new_content +=str(child)
            continue


        if child.name=="h2":
            current_title = child.string

        if child.name=="p": #close section
            new_content+=f'<section class="scrollspy mt-5" spy-title="{current_title}">{current_section}</section>'
            current_section=""

    return new_content


def content_addlinks(content):
    return content

def content_addimg(content):
    return content


def fpart(template, d_fit):
    """fits a template partically"""
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if var not in d_fit:
            print(f"proxied {var}")
            d_fit[var]= "{" + var + "}"
        else:
            print(f"available {var}")
    return template.format(**d_fit)


def get_files(path,ending=".docx"):
    a_results=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == ending:
                fullpath = os.path.join(root, f)
                a_results+=[f]
    return a_results

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

def create_blog(d_blog):
    """
    1. create individual blog pages bz rekursively fitting
    2. create index page
    3. output always copy to new file
    """

    #define content
    blog_url=d_blog["blog_url"]
    d_content = {
        "blog_logo": d_blog["blog_logo"],
        "blog_normal": d_blog["blog_normal"],
        "title": d_blog["blog_normal"],
        "head": "",
        "current_year": date.today().year,
    }
    d_content={**d_blog,**d_content}


    #define folder
    d_path={#path relative from the python program
        "iroot": f"{blog_url}",
        "iasset": f"asset",
        "oroot": f"../{blog_url}",
        "oblog": f"../{blog_url}/blog",
        "oasset": f"../{blog_url}/asset",
    }

    #create folder
    for key,val in d_path.items():
        try:
            Path(val).mkdir(parents=True, exist_ok=True) # output folder
        except:
            pass

    #remove old data from output folder if exist
    for to_delete in [d_path["oasset"], d_path["oblog"]]:
        for (root, dirs, files) in os.walk(to_delete, topdown=True):
            for file in files:
                os.remove(f"{root}/{file}")

    #copy latest asset (css, js) files to output
    copy_tree(d_path["iasset"],d_path["oasset"])

    #create input.xlsx automatically
    input_xlsx=f'{d_path["iroot"]}/input.xlsx'
    if os.path.isfile(input_xlsx):
        df_input=pd.read_excel(input_xlsx).set_index("document")
    else:
        df_input=pd.DataFrame(columns=["document","url","h1","published","comment"]).set_index("document")
        df_input.to_excel(input_xlsx)

    #update input.xlsx
    for file in get_files(d_path['iroot'],".docx"):
        document=str(file).replace(".docx","")
        url=document.lower()
        url=url.replace(" ","-")
        if document not in df_input.index:
            #if index doesn't exist, then assume other attributes are default
            #if index exists, other attributes can be manually channged
            df_input.at[document, "document"] = document
            df_input.at[document, "url"]=url
            df_input.at[document,"h1"]=document
            df_input.at[document,"published"]=time.strftime("%Y-%m-%d")
    df_input.to_excel(input_xlsx)

    #create blog article
    for index in df_input.index:
        # convert each docx input to html input
        #f = open(f"{d_path['iroot']}/{index}.docx", 'rb')
        if False:
            f = open(f"{d_path['iroot']}/{index}.docx", "r", encoding='utf-8').read()
            document = mammoth.convert_to_html(f)
            content = document.value.encode('utf8')
            output_file(page=content,filename=f"{d_path['iroot']}/{index}.html", pname=blog_url)
        elif False:
            with open(f"{d_path['iroot']}/{index}.docx", "rb") as docx_file:
                result = mammoth.extract_raw_text(docx_file)
                text = result.value  # The raw text
                with open(f"{d_path['iroot']}/{index}.html", 'w') as text_file:
                    text_file.write(text)

            content=get(f"{d_path['iroot']}/{index}.html",way=3)
        else:
            with open(f"{d_path['iroot']}/{index}.docx", "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                content = result.value


        #content modification
        content=content_h2list(content)
        content=content_scrollspy(content)
        content=content_addlinks(content)
        content=content_addimg(content)



        #make template
        pageBlog=get_template("pageBlog")
        pageBlog=resolve(pageBlog)

        #make content
        d_content_blog={
            "h1": df_input.at[index,"h1"],
            "title": df_input.at[index,"h1"],
            "published": df_input.at[index,"published"],
            "url_index": "../index.html",
            "img": "",
            #"content": get_content(pname=pname, file=index, way=3),
            "content":content,
            "toc": create_toc(content)
        }
        d_content_blog={**d_content,**d_content_blog}

        pageBlog = fpart(template=pageBlog,d_fit=d_content_blog)
        web_url=df_input.at[index,"url"]
        output_file(pageBlog, d_path["oblog"] + f"/{web_url}.html", pname=blog_url)


    #create index page
    a_articles = []
    for h1, url, published in zip(df_input["h1"], df_input["url"], df_input["published"]):
        d_article={
            "summary": "this is a summary of "+h1,
            "img": "",
            "href": f'blog/{url}.html',
            "h2": f"<a href='blog/{url}.html'>" + h1 + "</a>",
            "published": published,
        }
        blog_short = get_template(name="blog_short", way=3)
        a_articles += [blog_short.format(**d_article)]


    # fill the list until 3x elements so the list can be used for next function
    row_on_index = 3
    a_articles += [""] * (row_on_index - (len(a_articles) % row_on_index))

    columns = []
    for list_of_items in grouped(a_articles, row_on_index):
        list_with_col = [f'<div class="col">{x}</div>' for x in list_of_items]
        column = get_template(name="row_0",way=3).format("".join(list_with_col))
        columns += [column]

    d_content_index = {
        "url_index": "index.html",
        "_content": "".join(columns),
    }
    d_content_index = {**d_content, **d_content_index}
    pageIndex = get_template("pageIndex")
    pageIndex = resolve(pageIndex)
    pageIndex = fpart(pageIndex,d_content_index)
    output_file(pageIndex, d_path["oroot"] + f"/index.html", pname=blog_url)


if __name__ == '__main__':
    d_blog={
        "blog_url":"careercrashcourse.com",
        "blog_logo":"Career Crash Course",
        "blog_normal":"CareerCrashCourse",
    }
    create_blog(d_blog=d_blog)

