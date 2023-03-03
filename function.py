import pandas as pd
from data import *
import copy
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

def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)

def format_date(obj):
    return f"{obj.year}.{obj.month}.{obj.day}"

def article_toc(content):
    #this toc is only used for mobile version, for desktop version the toc is sticky
    result=""
    content=BeautifulSoup(content, "html.parser")
    for counter, h2 in enumerate(content.select("h2")):
        result=result+f"<li class='nodot'><a href='#header_{counter+1}'>"+h2.text+"</a></li>"
    return "<ul class='mt-3 bg-light mobile_toc' >Summary: "+result+"</ul>"

def article_firstparagraph(content):
    """get first paragraph of any content"""
    soup=BeautifulSoup(content, "html.parser")
    a_p=soup.findChildren("h2", recursive=True)
    for h2 in a_p:
        h2.string=""
    #result="".join([helper(x) for x in a_p if x.name !="h2"])
    return soup.getText()


def article_banner(content):
    """get first image of any content"""
    soup = BeautifulSoup(content, "html.parser")
    a_p = soup.findChildren("img", recursive=True)
    if a_p:
        return a_p[0]
    else:
        return ""


def get_helper(path="h1.html", way=3):
    if way == 1:  # get path for python
        return f"{path}"
    elif way == 2:  # get path for html rendering like img path
        return f"../{path}"
    elif way == 3:  # get file content itself
        return open(f"{path}", "r", encoding='utf-8').read()

def get(name, way=3):
    """get html template like h1.html"""
    if ".html" in  name:
        return get_helper(path=f"template/{name}", way=way)
    else:
        return get_helper(path=f"template/{name}.html", way=way)


def getc(name, way=3):
    """get component"""
    """get html template like h1.html"""
    if ".html" in  name:
        return get_helper(path=f"template/component/{name}", way=way)
    else:
        return get_helper(path=f"template/component/{name}.html", way=way)

def getcf(name, way=3, **kwargs):
    """get component"""
    """get html template like h1.html"""
    if ".html" in  name:
        template= get_helper(path=f"template/component/{name}", way=way)
    else:
        template= get_helper(path=f"template/component/{name}.html", way=way)
    template=template.format(**kwargs)

    return template


def get_files(path,ending=".docx"):
    a_results=[]
    for root, dirs, files in os.walk(path):
        for f in files:
            if os.path.splitext(f)[1] == ending:
                fullpath = os.path.join(root, f)
                a_results+=[f]
    return a_results


def save(page, filename, removehtml=False):
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

def pformat(template, d_fit):
    """fits a template partically"""
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if var not in d_fit:
            d_fit[var]= "{" + var + "}"
        else:
            pass
    return template.format(**d_fit)

def resolve_dict_automatic(d_data):
    """automatic resolve"""
    """ resolve the dict with form {function: data} to {data:data} """
    result=d_data.copy()
    for key,val in d_data.items():
        if callable(key):
            result[key.__name__]="".join(key(val,d_data))

    #after each solve, check data of each dict
    return result

"""
def resolve_dict_manual(d_data):
    manual resolve
    the resolve is manual, but it makes the dict very nice and good for translation

    1. all _stepn needs to be convereted to
    2. all _Qn and _An needs to be convereted to FAQ
    
    d_steps={x:y for x,y in d_data.items() if x.startswith("_step")}
    tool_steps = ""
    for counter, (stepcounter, component) in enumerate(d_steps.items()):
        component["stepnumber"]=counter+1
        tool_steps += get("component_tool_step.html").format(**component)
    d_data["tool_steps"] = pformat(tool_steps, d_website)

    d_helper = {**d_data, **d_general_faq}  # add general FAQ
    a_Q=[y for x,y in d_helper.items() if x.startswith("_Q")]
    a_A=[y for x,y in d_helper.items() if x.startswith("_A")]
    tool_faq = ""
    for counter, (question, answer) in enumerate(zip(a_Q,a_A)):
        tool_faq += get("component_tool_faq.html").format(**{
            "faq_number": counter + 1,
            "faq_question": "Q: "+question,
            "faq_answer": "A: "+answer,
        })
    d_data["tool_faq"] = pformat(tool_faq, d_website)
    return d_data #returns dict
"""

def resolve_dict_manual(tool, d_tool_s):
    """manual resolve
    the resolve is manual, but it makes the dict very nice and good for translation
    """

    #tool content
    d_tool_s["tool_steps"] = general_tool_content(tool, d_tool_s)

    #tool faq
    d_helper = {**d_tool_s, **d_tools_faq_g}  # add general FAQ
    a_Q=[y for x,y in d_helper.items() if x.startswith("_Q")]
    a_A=[y for x,y in d_helper.items() if x.startswith("_A")]
    tool_faq = ""
    for counter, (question, answer) in enumerate(zip(a_Q,a_A)):
        tool_faq += get("component_tool_faq.html").format(**{
            "faq_number": counter + 1,
            "faq_question": "Q: "+question,
            "faq_answer": "A: "+answer,
        })
    d_tool_s["tool_faq"] = pformat(tool_faq, d_website)
    return d_tool_s #returns dict



def resolve_template(template): #no use atm
    def get_d_template(way=3):
        """returns all template as dict
        way 1. key = page.html, val =html content
        way 2. key = page, val =html content
        way 3. key = $page, val =html content
        """
        d_template = {}
        a_template = get_files(path="template", ending=".html")
        for template in a_template:
            d_way = {
                1: template,
                2: template.replace(".html", ""),
                3: "$" + template.replace(".html", ""),
            }
            d_template[d_way[way]] = get(template)
        return d_template

    """resolves a template and fits all his modules"""
    a_replaced=[]
    d_template=get_d_template(way=3)
    for var in [fn for _, fn, _, _ in Formatter().parse(template) if fn is not None]:
        if "$" in var  and var in d_template.keys():
            a_replaced+=[var]
        else:
            d_template[var]="{"+var+"}"
    template = template.format(**d_template)

    return resolve_template(template) if len(a_replaced) > 0 else template



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


def content_scrollspy(content,index):
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


def content_addlinks(content,index):
    return content

def content_addimgalt(content,index):
    """add alt attribute to images"""
    soup = BeautifulSoup(content, "html.parser")
    a_img = soup.find_all("img")
    for counter,img in enumerate(a_img):
        img["alt"] = f"{index} {counter}"
    return str(soup)

def content_target_blank(content,index):
    """makes all links open externally in browser and not replace current browser
    """
    soup=BeautifulSoup(content, "html.parser")
    a_a=soup.find_all("a")
    for a in a_a:
        a["target"]="_blank"
    return str(soup)


def nav(a_li,d_website):
    result=[]
    for li in a_li:
        nav_li=pformat(get("nav_li.html"), li)
        result+=[nav_li]
    result="".join(result)
    result= pformat(get("nav.html"), {"navli":result})
    result=pformat(result,d_website)
    return result


def tool_index_content():
    """go through all available tools and create one col for it"""
    result=''
    for data in d_tools_txt_s:
        d_replace={
            "tool": data["tool"],
            "h1":data["h1"],
            "h1description":data["h1description"],
        }
        result+=pformat(get("card.html"), d_replace)
    return result


def create_blog(d_website):
    """
    1. create individual blog pages bz rekursively fitting
    2. create index page
    3. output always copy to new file
    """

    """---------------- folder manipulation here ----------------"""
    #define content
    d_website={**d_website, **d_websites_g}
    d_website= resolve_dict_automatic(d_website)

    #define folder
    d_expath={#path relative from the python program
        "iroot": f"{d_website['blog_url']}",
        "isasset": f"{d_website['blog_url']}/asset", #input of Specific asset
        "iasset": f"asset", #input of General Asset
        "oroot": f"../{d_website['blog_url']}",
        "oblog": f"../{d_website['blog_url']}/blog",
        "oasset": f"../{d_website['blog_url']}/asset",
    }

    #is needed, don't remove
    for key, val in d_expath.items():
        if not os.path.isdir(val):
            Path(val).mkdir(parents=True, exist_ok=True)  # output folder

    #remove old data from output folder if exist
    for to_delete in [d_expath["oasset"], d_expath["oblog"]]:
        for (root, dirs, files) in os.walk(to_delete, topdown=True):
            for file in files:
                os.remove(f"{root}/{file}")

    #remove old data from root directory, todo make this delete function more compact
    for to_delete in [d_expath["oroot"]]:
        for (root, dirs, files) in os.walk(to_delete, topdown=True):
            for file in files:
                if ".html" in file:
                    os.remove(f"{root}/{file}")


    #copy latest asset (css, js) files to output
    copy_tree(d_expath["iasset"],d_expath["oasset"])
    copy_tree(d_expath["isasset"], d_expath["oasset"])

    #create input.xlsx automatically
    input_xlsx=f'{d_expath["iroot"]}/input.xlsx'
    df_input=pd.DataFrame(columns=["document","url","h1","published","comment"]).set_index("document")
    df_input.to_excel(input_xlsx)

    #update input.xlsx
    for file in get_files(d_expath['iroot'],".docx"):
        document=(str(file)
                  .replace(".docx","")
                  .lower())
        url = (remove_leadingnumber(document)
               .lstrip()
               .replace(" ","-"))

        published = os.path.getmtime(d_expath['iroot']+"/"+file)
        published=datetime.datetime.fromtimestamp(published)

        updated = os.path.getctime(d_expath['iroot'] + "/" + file)
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


    """---------------- create blog article here ----------------"""

    #blog article
    d_summary={}
    d_banner={}
    for index in df_input.index:
        # convert each docx input to html input
        with open(f"{d_expath['iroot']}/{index}.docx", "rb") as docx_file:
            content = mammoth.convert_to_html(docx_file).value

        #content modification
        for func  in [content_h2list, content_scrollspy, content_addlinks, content_addimgalt,content_target_blank ]:
            content=func(content,index)

        #make content
        d_blog_article={
            "h1": df_input.at[index,"h1"],
            "title": d_website["title"],
            "published": format_date(df_input.at[index,"published"]),
            "updated": format_date(df_input.at[index,"updated"]),
            "img": "",
            "read_time": read_time(content),
            "content":content,
            "toc": article_toc(content)
        }

        #save everthing
        d_summary[index]=article_firstparagraph(content) # returns the first parahraph of the content
        d_banner[index]=article_banner(content)
        d_blog_article={**d_website,**d_blog_article}
        pageBlogArticle = pformat(get("page_blog_article.html"), d_blog_article)
        save(pageBlogArticle, d_expath["oblog"] + f"/{df_input.at[index, 'url']}.html")


    #blog index page todo can be optimized in dict
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
        blog_short = get(name="col2.html", way=3)
        a_articles += [blog_short.format(**d_article)]
    columns = "".join([f"<div class='col col-md-4 row_index mb-5'>{x}</div>" for x in a_articles])
    d_blog_index = {**d_website, **{"blog_index_content": columns, }}
    pageBlogIndex = pformat(get("page_blog_index.html"), d_blog_index)
    save(pageBlogIndex, d_expath["oroot"] + f"/blog/index.html")

    #website index page
    pageIndex = pformat(get("page_index.html"), d_blog_index)
    save(pageIndex, d_expath["oroot"] + f"/index.html")



    """---------------- create Tools here ----------------"""

    #tool function
    if d_website["blog_url"]== "sicksheet.com":
        #generate individual tool
        for d_tool in d_tools_txt_s:
            tool=d_tool["tool"]
            #create the final replacement dict to replace the template
            d_tool = resolve_dict_manual(tool=tool, d_tool_s=d_tool) # resolve dict to make function out of dict data
            d_tool={**d_website,**d_tool} #merge dicts together. second thing overwrites first

            page_tool = pformat(get("page_tool_function.html"), {"toolbody": get("component_tool.html")})
            page_tool = pformat(page_tool, d_tool)
            save(page_tool, d_expath["oroot"] + f"/{tool}.html")

        #tool index
        page_tool_index = get("page_tool_index.html")
        page_tool_index = pformat(page_tool_index, {**d_blog_index, **{"cols":tool_index_content()}})
        save(page_tool_index, d_expath["oroot"] + f"/tools/index.html")



def general_tool_content(tool, d_tool_txt_s):
    """one of the main tools"""
    """returning normal template
    1. takes Data
    2. takes html template
    3. outputs general page content
    """

    #specific text + standard text
    d_tool_txt_s={**d_tools_txt_g, **d_tool_txt_s} #add normal data and specific data togehter

    #standard content:  3 steps.
    d_tool_content_g={
        "input.content":getcf("hot.html",id="table1"),
        "configure.content":"no specific config",
        "download.content":getcf("hot.html",id="table2")+getcf("button.html",id="download",label="Download"),
    }

    #specific content
    nohyphen=tool.replace("-","_")#use - for url, and _ for python
    if nohyphen in globals().keys():
        f_tool = globals()[nohyphen]
        d_tool_content_s,d_tool_txt_s=f_tool(copy.deepcopy(d_tool_content_g),copy.deepcopy(d_tool_txt_s))
    else:
        d_tool_content_s = d_tool_content_g


    #Heirat: merge content and template together to step
    d_result={}
    counter=1
    for key in ["input","input2","configure","download"]: #input2 only used for join.
        if not [x for x in d_tool_txt_s.keys() if x.startswith(f"{key}.")]:
            continue
        d_result[key]=get("component_tool_step.html").format(**{
            "step_n":counter,
            "step_h1":d_tool_txt_s[f"{key}.title"],
            "step_descr":d_tool_txt_s[f"{key}.descr"],
            "step_data": d_tool_content_s[f"{key}.content"],
        })
        counter+=1
    return "".join(d_result.values())


def join_tables(d_html, d_txt):
    # change input 1 text
    #done in table

    #create custom step
    d_html["input2.content"] = getcf("hot.html", id="table2")+getcf("alert.html", id="leftalert",label="")

    #add configure
    select=getcf("select.html", id="jointype",)
    img = getcf("img.html", id="joinimg", alt="Join type image as Venn Diagram", src="", width="100%", height="",)
    d_html["configure.content"] = select + img

    #change download
    table3 = getcf("hot.html", id="table3")
    download = getcf("button.html", id="download", label="Download")
    d_html["download.content"] = table3 + download
    return [d_html, d_txt]


def transpose_table(d_html, d_txt):
    for key in list(d_html.keys()):
        if key.startswith("configure."):
            d_html.pop(key)

    for key in list(d_txt.keys()):
        if key.startswith("configure."):
            d_txt.pop(key)
    return [d_html, d_txt]


def sort_rows(d_html, d_txt):
    slide1=getcf("select.html",id="sortcol")
    slide2=getcf("select.html",id="asc")
    d_html["configure.content"]= slide1 + slide2
    return [d_html, d_txt]

def first_n_rows(d_html, d_txt):
    range = getcf("range.html", id="n", label="First n Rows")
    d_html["configure.content"] = range
    return [d_html, d_txt]

def last_n_rows(d_html, d_txt):
    range = getcf("range.html", id="n",label="Last n Rows")
    d_html["configure.content"] = range
    return [d_html, d_txt]

def slice_rows(d_html, d_txt):
    range1 = getcf("range.html", id="startn", label="Start at Row n")
    range2 = getcf("range.html", id="endn", label="End at Row n")
    d_html["configure.content"] = range1 + range2
    return [d_html, d_txt]

def sample_rows(d_html, d_txt):
    range = getcf("range.html", id="n", label="Sample n Rows")
    button = getcf("button.html", id="sample", label="Sample Rows")
    d_html["configure.content"] = range + button
    return [d_html, d_txt]

def shuffle_rows(d_html, d_txt):
    button = getcf("button.html", id="shuffle", label="Shuffle Row")
    d_html["configure.content"] = button
    return [d_html, d_txt]

def drop_duplicated_columns(d_html, d_txt):
    for key in list(d_html.keys()):
        if key.startswith("configure."):
            d_html.pop(key)

    for key in list(d_txt.keys()):
        if key.startswith("configure."):
            d_txt.pop(key)
    return [d_html, d_txt]




if __name__ == '__main__':
    for d_website in d_websites_s:
        if d_website["blog_url"] =="sicksheet.com":
            create_blog(d_website=d_website)

