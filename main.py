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




def create_toc(content):
    #this toc is only used for mobile version, for desktop version the toc is sticky
    result=""
    content=BeautifulSoup(content)
    for counter, h2 in enumerate(content.select("h2")):
        result=result+f"<li class='nodot'><a href='#header_{counter+1}'>"+h2.text+"</a></li>"
    return "<ul class='mt-3 bg-light mobile_toc' >Summary: "+result+"</ul>"


def get( path="h1.html", purpose=3):
    if purpose==1: #get path for python
        return f"{path}"
    elif purpose==2: #get path for html rendering like img path
        return f"../{path}"
    elif purpose ==3: #get file content itself
        return open(f"{path}", "r", encoding='utf-8').read()


def to_page(page,filename):
    Path(f"blog").mkdir(parents=True, exist_ok=True)
    with open(fr"blog/{filename}.html", "w", encoding="utf-8") as file:
        file.write(str(page))


def create_blog():
    """
    1. create individual blog pages bz rekursively fitting
    2. create index page
    3. output
    """

if __name__ == '__main__':
    create_blog()