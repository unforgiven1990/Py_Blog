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
    content=BeautifulSoup(content)
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

def get_content(pname, file, way=3):
    """get content like how tocebome project manager.html"""
    if ".html" in  file:
        return get(path=f"{pname}/{file}", way=way)
    else:
        return get(path=f"{pname}/{file}.html", way=way)


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
            print(f"{var} in replace array")
            a_replaced+=[var]
        else:
            d_template[var]="{"+var+"}"
    template = template.format(**d_template)

    return resolve(template) if len(a_replaced) >0 else template


def fpart(template, d_fit):
    """fits a template partically"""
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if var not in d_fit:
            print(f"proxied {var}")
            d_fit[var]= "{" + var + "}"
        else:
            print(f"available {var}")
    print(template)
    return template.format(**d_fit)


def get_files(path,ending=".docx"):
    a_results=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == ending:
                fullpath = os.path.join(root, f)
                a_results+=[f]
    return a_results


def create_blog(pname):
    """
    1. create individual blog pages bz rekursively fitting
    2. create index page
    3. output always copy to new file
    """

    #create folder
    path={#path relative from the python program
        "iroot": f"{pname}",
        "iasset": f"{pname}/asset",
        "input.xlsx": f"{pname}/input.xlsx",
        "oroot": f"../{pname}",
        "oblog": f"../{pname}/blog",
        "oasset": f"../{pname}/asset",
    }

    Path(path["iroot"]).mkdir(parents=True, exist_ok=True) # input folder
    Path(path["oroot"]).mkdir(parents=True, exist_ok=True) # output folder

    #clean up every folder except .idea
    for (root, dirs, files) in os.walk(path["oroot"], topdown=True):
        for dir in dirs:
            if ".idea" != dir:
                print(f"delete {root}/{dir} ")
                #os.remove(f"{root}/{dir}")

    #todo. atm manually delete asset and blog folder


    #create input xlsx automatically
    if os.path.isfile(path["input.xlsx"]):
        df_input=pd.read_excel(path["input.xlsx"]).set_index("index")
    else:
        df_input=pd.DataFrame(columns=["index","url","h1","published","comment"]).set_index("index")
        df_input.to_excel(path["input.xlsx"])


    #update input.xlsx
    for file in get_files(path['iroot'],".docx"):
        index=str(file).replace(".docx","")
        if index not in df_input.index:
            #if index doesn't exist, then assume other attributes are default
            #if index exists, other attributes can be manually channged
            df_input.at[index,"url"]=index
            df_input.at[index,"h1"]=index
            df_input.at[index,"published"]=time.strftime("%Y-%m-%d")
    df_input.to_excel(path["input.xlsx"])





    # now create blog
    for index in df_input.index:
        # convert each docx input to html input
        f = open(f"{path['iroot']}/{index}.docx", 'rb')
        content = mammoth.convert_to_html(f).value.encode('utf8')

        #make template
        pageBlog=get_template("pageBlog")
        pageBlog=resolve(pageBlog)


        #make content
        d_content={
            "blog": pname,
            "h1": df_input.at[index,"h1"],
            "title": df_input.at[index,"h1"],
            "head": "",
            "current_year": date.today().year,
            "published": df_input.at[index,"published"],
            #"content": get_content(pname=pname, file=index, way=3),
            "content":content,
        }

        pageBlog = fpart(template=pageBlog,d_fit=d_content)
        output_file(pageBlog, path["oblog"] + f"/{index}.html", pname=pname)




if __name__ == '__main__':
    create_blog(pname="careercrashcourse.com")

