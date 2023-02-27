import pandas as pd
from data import *
import numpy as np
from bs4 import BeautifulSoup
import selenium
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import os.path
from selenium import webdriver
from distutils.dir_util import copy_tree
import os, time, datetime
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


def read_time(content):
    def myround(x, base=0.5):
        return base * round(x / base)

    words=len(content.split(" "))
    speed=250 #per min
    min=words/speed
    min=myround(min,base=0.5)
    if min.is_integer():
        min=int(min)
    return f"{min} min read"

def cut_summary(summary, maxlen=50):
    if len(summary) < maxlen:
        return summary
    traversed_chars=''
    for char in summary:
        traversed_chars+=char
        break_loop = True if len(traversed_chars) > maxlen else False
        if break_loop and char==" ":
            return traversed_chars +"..."
    return traversed_chars +" ..." # should stop but didnt found any whitespace to stop



def remove_leadingnumber(url):
    from string import digits
    return url.lstrip(digits)


def create_toc(content):
    #this toc is only used for mobile version, for desktop version the toc is sticky
    result=""
    content=BeautifulSoup(content, "html.parser")
    for counter, h2 in enumerate(content.select("h2")):
        result=result+f"<li class='nodot'><a href='#header_{counter+1}'>"+h2.text+"</a></li>"
    return "<ul class='mt-3 bg-light mobile_toc' >Summary: "+result+"</ul>"

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

def format_date(obj):
    return f"{obj.year}.{obj.month}.{obj.day}"

def get_firstparagraph(content):
    """get first paragraph of any content"""
    soup=BeautifulSoup(content, "html.parser")
    a_p=soup.findChildren("h2", recursive=True)
    for h2 in a_p:
        h2.string=""
    #result="".join([helper(x) for x in a_p if x.name !="h2"])
    return soup.getText()


def get_banner(content):
    """get first image of any content"""
    soup = BeautifulSoup(content, "html.parser")
    a_p = soup.findChildren("img", recursive=True)
    if a_p:
        return a_p[0]
    else:
        return ""



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

def get_files(path,ending=".docx"):
    a_results=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == ending:
                fullpath = os.path.join(root, f)
                a_results+=[f]
    return a_results


def output_file(page, filename, removehtml=False):
    if removehtml:
        filename=filename.replace(".html")

    # two slashes means root e.g. ../sicksheet.com/index.html
    #if more than 2 slashes , then add 1 slash back to every url
    if filename.count("/")>2:
        #replace all url
        soup=BeautifulSoup(page, "html.parser")

        #replace elements in nav
        nav=soup.find("nav")
        for a in nav.find_all("a"):
            a['href'] = "../"+a['href']
        page = str(soup)

        # replace elements in head Script
        head = soup.find("head")
        for script in head.find_all("script"):
            if "https" not in script["src"]:
                script['src'] = "../" + script['src']

        # replace elements in head Script
        head = soup.find("head")
        for link in head.find_all("link"):
            if "https" not in link["href"]:
                link['href'] = "../" + link['href']

        page = str(soup)


    #calculate all url as if they are from root, then adjust to relative path locally in python to make it locally visible without localhost. online works anyway
    # if  inpu is root/index.html, then replace ../ with /
    # if  inpu is root/folder/index.html, then all url without ../

    #check if directory exists
    directory="/".join([x for x in filename.split("/")[:-1]])
    if not os.path.isdir(directory):
        Path(directory).mkdir(parents=True, exist_ok=True)

    with open(fr"{filename}", "w", encoding="utf-8") as file:
        file.write(str(page))

def fpart(template, d_fit):
    """fits a template partically"""
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if var not in d_fit:
            d_fit[var]= "{" + var + "}"
        else:
            pass
    return template.format(**d_fit)


def resolve(template):
    """resolves a template and fits all his modules"""
    a_replaced=[]
    d_template=get_d_template(way=3)
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if "$" in var  and var in d_template.keys():
            a_replaced+=[var]
        else:
            d_template[var]="{"+var+"}"
    template = template.format(**d_template)

    return resolve(template) if len(a_replaced) >0 else template



def content_h2list(content, index):
    """
    add a list to all h2 titles

    """
    soup = BeautifulSoup(content, 'html.parser')
    for counter, h2 in enumerate(soup.find_all(name="h2")):
        formated_h2=[]

        try :
            h2.string.split(" ")
        except:
            print(f"{index} bugged")
            continue

        for word in h2.string.split(" "):
                if not word.isupper():
                    formated_h2+=[word.title()]
                else:
                    formated_h2 += [word]
        formated_h2=" ".join(formated_h2)

        #check if old title already has enumeration
        first=formated_h2[0:1]
        if first in "0123456789":
            formated_h2=formated_h2[2:]

        formated_h2=formated_h2[:-1] if formated_h2[-1]==":" else formated_h2
        h2.string=f"{counter+1}. {formated_h2}"

    return str(soup)


def content_scrollspy(content):
    """
    1. the generated html file is not directly scrollspyable
    2. convert <h2><p> to <section><h2><p></section>
    3. the first element of any document must be h2,everything before will be disregarded
    also returns the first paragraph of the text which can be summarized later
    """
    soup=BeautifulSoup(content,'html.parser')
    new_content=""
    current_section=""
    current_title=""
    for child in soup.findChildren(recursive=False):
        if child.name=="h2":#open section by h2 or still opened
            # close previous section
            if current_title: # check to prevent first h2 having not title
                new_content += f'<section class="scrollspy mt-5" spy-title="{current_title}">{current_section}</section>'
                current_section = "" #reset

            # open new section
            current_title = child.string
            current_section += str(child)
        else:# element is not h2, will all be moved together
            current_section += str(child)
    else:
        new_content += f'<section class="scrollspy mt-5" spy-title="{current_title}">{current_section}</section>'
    return new_content


def content_addlinks(content):
    return content

def content_addimgalt(content,index):
    """add alt attribute to images"""
    soup = BeautifulSoup(content, "html.parser")
    a_img = soup.find_all("img")
    for counter,img in enumerate(a_img):
        img["alt"] = f"{index} {counter}"
    return str(soup)

def content_target_blank(content):
    """makes all links open externally in browser and not replace current browser
    """
    soup=BeautifulSoup(content, "html.parser")
    a_a=soup.find_all("a")
    for a in a_a:
        a["target"]="_blank"
    return str(soup)














def create_blog(d_blog):
    """
    1. create individual blog pages bz rekursively fitting
    2. create index page
    3. output always copy to new file
    """

    #define content
    blog_url=d_blog["blog_url"]
    d_content = {
        "title": d_blog["blog_normal"],
        "head": "",
        "current_year": date.today().year,
        "url_index": "index.html",
        "url_blog": "blog/index.html",
    }

    d_content={**d_blog,**d_content}


    #define folder
    d_path={#path relative from the python program
        "iroot": f"{blog_url}",
        "isasset": f"{blog_url}/asset", #input of Specific asset
        "iasset": f"asset", #input of General Asset
        "oroot": f"../{blog_url}",
        "oblog": f"../{blog_url}/blog",
        "oasset": f"../{blog_url}/asset",
    }

    #is needed, don't remove
    for key, val in d_path.items():
        if not os.path.isdir(val):
            Path(val).mkdir(parents=True, exist_ok=True)  # output folder

    #remove old data from output folder if exist
    for to_delete in [d_path["oasset"], d_path["oblog"]]:
        for (root, dirs, files) in os.walk(to_delete, topdown=True):
            for file in files:
                os.remove(f"{root}/{file}")


    #copy latest asset (css, js) files to output
    copy_tree(d_path["iasset"],d_path["oasset"])
    copy_tree(d_path["isasset"], d_path["oasset"])

    #create input.xlsx automatically
    input_xlsx=f'{d_path["iroot"]}/input.xlsx'
    df_input=pd.DataFrame(columns=["document","url","h1","published","comment"]).set_index("document")
    df_input.to_excel(input_xlsx)


    #update input.xlsx
    for file in get_files(d_path['iroot'],".docx"):
        document=str(file).replace(".docx","")
        url=document.lower()
        url = remove_leadingnumber(url).lstrip()
        url=url.replace(" ","-")


        published = os.path.getmtime(d_path['iroot']+"/"+file)
        published=datetime.datetime.fromtimestamp(published)

        updated = os.path.getctime(d_path['iroot'] + "/" + file)
        updated = datetime.datetime.fromtimestamp(updated)

        if document not in df_input.index:
            #if index doesn't exist, then assume other attributes are default
            #if index exists, other attributes can be manually channged
            df_input.at[document, "document"] = document
            df_input.at[document, "url"]=url
            df_input.at[document, "h1"]=document.title()
            df_input.at[document, "published"]=published
            df_input.at[document, "updated"]=updated
    df_input=df_input.sort_values("published", ascending=False)
    df_input.to_excel(input_xlsx)



    #create nav dynamically for all webpages
    nav_element1 = fpart(get_template("navLi.html"),{"nav_text":"Blog","nav_url":"blog/index.html"})
    if d_blog["blog_url"]=="sicksheet.com":
        nav_element2 = fpart(get_template("navLi.html"),{"nav_text":"Tools", "nav_url":"tools/index.html"})
    else:
        nav_element2=""
    d_content["navli"]="".join([nav_element2, nav_element1])
    nav = fpart(get_template("nav.html"),d_content)
    d_content["nav"] = nav


    #create blog article
    d_summary={}
    d_banner={}
    for index in df_input.index:
        # convert each docx input to html input
        with open(f"{d_path['iroot']}/{index}.docx", "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
            content = result.value

        #content modification
        content=content_h2list(content,index)
        content=content_scrollspy(content)
        content=content_addlinks(content)
        content=content_addimgalt(content,index)
        content=content_target_blank(content)

        #make content
        d_content_blog={
            "h1": df_input.at[index,"h1"],
            "title": d_content["blog_normal"],
            "published": format_date(df_input.at[index,"published"]),
            "updated": format_date(df_input.at[index,"updated"]),
            "img": "",
            "read_time": read_time(content),
            #"content": get_content(pname=pname, file=index, way=3),
            "content":content,
            "toc": create_toc(content)
        }
        d_summary[index]=get_firstparagraph(content) # returns the first parahraph of the content
        d_banner[index]=get_banner(content)
        d_content_blog={**d_content,**d_content_blog}

        # make template
        pageBlogArticle = get_template("pageBlogArticle.html")
        pageBlogArticle = resolve(pageBlogArticle)
        pageBlogArticle = fpart(template=pageBlogArticle,d_fit=d_content_blog)
        output_file(pageBlogArticle, d_path["oblog"] + f"/{df_input.at[index,'url']}.html")


    #create blog index page
    a_articles = []
    for index,h1, url, published in zip(df_input.index, df_input["h1"], df_input["url"], df_input["published"]):
        d_article={
            "summary": cut_summary(d_summary[index],maxlen=150),
            "metadescription": cut_summary(d_summary[index],maxlen=150),
            "metakeywords": h1,
            "banner": d_banner[index],
            "img": "",
            "href": f'{url}.html',
            "h2": f"<a href='{url}.html'>" + h1 + "</a>",
            "published": format_date(published),
        }
        blog_short = get_template(name="indexBlogItem.html", way=3)
        a_articles += [blog_short.format(**d_article)]
    columns = "".join([f"<div class='col col-md-4 row_index mb-5'>{x}</div>" for x in a_articles])
    d_content_index = {
        "url_index": "index.html",
        "_content": columns,
    }
    d_content_index = {**d_content, **d_content_index}
    pageBlogIndex = get_template("pageBlogIndex.html")
    pageBlogIndex = resolve(pageBlogIndex)
    pageBlogIndex = fpart(pageBlogIndex,d_content_index)
    output_file(pageBlogIndex, d_path["oroot"] + f"/blog/index.html")


    #index page
    pageIndex = get_template("pageIndex.html")
    if d_blog["blog_url"]=="sicksheet.com":
        d_page_index = {
            "redirect": "tools/index.html",
            "title": d_blog["blog_url"],
        }
    else:
        d_page_index = {
            "redirect":"blog/index.html",
            "title": d_blog["blog_url"],
        }
    d_page_index={**d_page_index,**d_content_index}
    pageIndex = fpart(pageIndex, d_page_index)
    output_file(pageIndex, d_path["oroot"] + f"/index.html")


    if d_blog["blog_url"]=="sicksheet.com":
        for tool in ["join","transpose"]:
            pageExcel = get_template("pageSheet.html")
            pageExcel = fpart(pageExcel, {"toolbody": "{$tool_"+tool+"}"})
            pageExcel = resolve(pageExcel)
            d_meta_join={
                "metadescription":"A online free tool that merges two spreadsheets together. The tool is easy to use, free and purely online.",
                "metakeywords":"Online, Spreadsheet, Tool, Join, Merge",
            }
            d_content_join={**d_meta_join,**d_content_index}
            pageExcel = fpart(pageExcel, d_content_join)
            output_file(pageExcel, d_path["oroot"] + f"/{tool}.html")


        #create Tool Index
        pageToolIndex = get_template("pageToolIndex.html")
        pageToolIndex = resolve(pageToolIndex)
        pageToolIndex = fpart(pageToolIndex, d_content_index)
        output_file(pageToolIndex, d_path["oroot"] + f"/tools/index.html")



if __name__ == '__main__':
    for d_blog in data_websites:
        create_blog(d_blog=d_blog)

