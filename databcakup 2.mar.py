from datetime import *
from main_page import get,getc,getcf, pformat
"""
blog data are stored in word files
tool data are stored in dict/obj
website meta data are stored in dict
"""

def nav(a_li,d_website):
    result=[]
    for li in a_li:
        nav_li=pformat(get("nav_li.html"), li)
        result+=[nav_li]
    result="".join(result)
    result= pformat(get("nav.html"), {"navli":result})
    result=pformat(result,d_website)
    return result

#todo deprecated remove it
def tool_steps(tooldata,d_website):
    result=""
    for counter, (key, d_step) in enumerate(tooldata.items()):
        if callable(key):
            d_step=key()

        onestep=get("component_tool_step.html").format(**{
            "stepnumber":counter+1,
            "steptitle": d_step["steptitle"],
            "stepdescription":d_step["stepdescription"],
            "stepcontent":d_step["stepcontent"],
        })
        result+=onestep
    result = pformat(result, d_website)
    return result


#todo deprecated remove it
def tool_faq(tooldata,d_website):
    result = ""
    #get the generla QA
    d_all_AQ={**tooldata, **d_general_faq}
    for counter, (question,answer) in enumerate(d_all_AQ.items()):
        oneQA = get("component_tool_faq.html").format(**{
            "faq_number": counter+1,
            "faq_question": question,
            "faq_answer": answer,
        })
        result += oneQA
    result = pformat(result, d_website)
    return result



def c_input(steptitle="Input", stepdescription="Copy paste your table here.",stepcontent='<div id="table1"></div>'):
    return {"steptitle":steptitle,
             "stepdescription":stepdescription,
             "stepcontent":stepcontent,
             }

def c_configure(steptitle="Configure",stepdescription="Configure the options.",stepcontent="empty todo"):
    return {"steptitle":steptitle,
              "stepdescription":stepdescription,
              "stepcontent":stepcontent,
              }

def c_download(steptitle="Download",stepdescription="Copy or Download your result in CSV.",tableid="table2"):
    return {
        "steptitle": steptitle,
        "stepdescription": stepdescription,
        "stepcontent": f'<div id="{tableid}"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
        }


def c_slider(label="Last n Rows"):
    return {
        "steptitle": "Configure",
        "stepdescription": "Configure your options",
        "stepcontent": f"""
        <div class="form-group">
      <label class="control-label col" for="n">{label}:</label>
      <div class="col">
       <input id="n" type="range" class="form-range" min="1" max="100">
        </div>
    </div>""",
    }


d_normal={
    "input.title":"Input",
    "input.descr":"Copy paste your table here.",
    "input.content":getcf("hot.html",id="table1"),
    "configure.title":"Configure",
    "configure.descr":"Configure the options.",
    "configure.content":"",
    "download.title":"Download",
    "download.descr":"Copy or Download your result in CSV.",
    "download.content":getcf("hot.html",id="table2"),
}


d_tools={
    "join":{
        "tool":"join",
        "h1":"Join Tables",
        "h1description": "Merge and join two spreadsheets based on their key column.",
        "title": "Join Table Online",
        "metadescription": "An free online tool to join spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Join, Merge",
        "_Q1": "What is the difference between Left Join, Right Join, Inner Join and Outer Join?",
        "_A1": """<ul>
          <li><b>Inner Join</b>: Returns records that have matching values in <b>both tables</b></li>
          <li><b>Left (Outer) Join</b>: Returns all records from the <b>left table</b>, and the matched records from the right table</li>
          <li><b>Right (Outer) Join</b>: Returns all records from the <b>right table</b>, and the matched records from the left table</li>
          <li><b>Full (Outer) Join</b>: Returns all records when there is a match in <b>either left or right table</b></li>
        </ul>""",
        "_Q2":"I uploaded both sheets, but it doesn't produce results.",
        "_A2":"A: Make sure the key of each sheet is in the first column and that they are named <b>exactly the same</b>. You can edit the column name in the online table directly.",
        "_step1": c_input("Input Left Table","Copy paste your first table here."),
        "_step2": c_input("Input Left Right","Copy paste your second table here.",'<div id="table2"></div><div id="leftalert" class="alert alert-danger leftalert"></div>'),
        "_step3": c_configure(stepcontent=get("configure/join.html")),
        "_step4": c_download(tableid="table3")
    },


    "transpose":{
        "tool":"transpose",
        "h1":"Transpose Tables",
        "h1description": "Swap spreadsheet column and row axis.",
        "title": "Transpose Table Online",
        "metadescription": "An free online tool to transpose spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Transpose",
        "_step1": c_input(),
        "_step2": c_download(),
    },


    "sort":{
        "tool":"sort",
        "h1":"Sort Tables",
        "h1description": "Sort spreadsheet columns in ascending or descending order.",
        "title": "Sort Table Online",
        "metadescription": "An free online tool to sort spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Sort",
        "_step1": c_input(),
        "_step2": c_configure(stepcontent=get("configure/sort.html")),
        "_step3": c_download(),

    },

    "tail":{
        "tool":"tail",
        "h1":"Last n Rows",
        "h1description": "Get the last n rows of a spreadsheet.",
        "title":"Get Last n Rows Online",
        "metadescription": "An free online tool to get the last n rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Tail, last row",
        "_step1":c_input(),
        "_step2":c_slider(),
        "_step3":c_download(),
    },


        "sample":{
        "tool":"sample",
        "h1":"Get Sample Rows",
        "h1description": "Get a sampled subset of rows in a spreadsheet",
        "title":"Get a sampled subset of rows in a spreadsheet",
        "metadescription": "An free online tool to get a sampled rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Sample, Subset",
        "_step1":c_input(),
        "_step2":c_slider(label="Sample n Percent"),
        "_step3":c_download(),
    },


    "head":{
        "tool":"head",
        "h1":"First n Rows",
        "h1description": "Get the first n rows of a spreadsheet.",
        "title":"Get First n Rows Online",
        "metadescription": "An free online tool to get the first n rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Head, first row",
        "_step1":c_input(),
        "_step2":c_slider(label="First n Rows"),
        "_step3":c_download(),
    },

    "slice": {
        "tool": "slice",
        "h1": "Slice Rows",
        "h1description": "Get a subset of Consecutive Rows.",
        "title": "Get a subset of Consecutive Rows.",
        "metadescription": "An free online tool to get the first n rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Slice",
        "_step1.title": d_normal["input.title"],
        "_step1.descr": d_normal["input.descr"],
        "_step1.content": d_normal["input.content"],
        "_step2.title": d_normal["configure.title"],
        "_step2.descr": d_normal["configure.descr"],
        "_step2.content": d_normal["configure.content"],
        "_step3.title": d_normal["download.title"],
        "_step3.descr": d_normal["download.descr"],
        "_step3.content": d_normal["download.content"],
    },



        "shuffle":{
        "tool":"shuffle",
        "h1":"Shuffle Table Rows",
        "h1description": "Randomly shuffle rows of your spreadsheet.",
        "title":"Randomly shuffle rows of your spreadsheet.",
        "metadescription": "An free online tool to shuffle the rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Shuffle, Random",
        "_step1":c_input(),
        "_step2":c_configure(stepcontent='<button id="shuffle" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" >Shuffle Rows</button>'),
        "_step3":c_download(),
    },


    "drop duplicated columns":{
        "tool":"drop duplicated columns",
        "h1":"Drop Duplicated Columns",
        "h1description": "Remove columns with the same name",
        "title":"Drops duplicated rows for a selected column.",
        "metadescription": "An free online tool to drop duplicated rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Drop Duplicates, Remove Duplicates",
        "_step1":c_input(),
        #"_step2":c_configure(stepcontent=get("configure/drop_duplicates.html")),
        "_step3":c_download(),
    },
}



d_general_faq={
            "_Q100":"Can I upload my data as .xlsx or .csv file?",
            "_A100":"Upload data as .xlsx or .csv file is not supported yet. You can copy paste your data from excel into the website table above.",
            "_Q101":"Can it handle big data sets?",
            "_A101":"Upload data as .xlsx or .csv file is not supported yet.   A: Yes it can handle tables up to 6000 columns and rows. If you encounter lag, you can reduce the sheet size.",
            "_Q102":"It is normal that it lags a couple of seconds during copy paste?",
            "_A102":"Yes this is normal for a web based application (especially when the data set is large).",
            "_Q103":"The provided spreadsheet interface is very small. Can you make it bigger?",
            "_A103":"It is recommended to paste data into Excel to manage a bigger data sets.",
            "_Q104":"What plugin do you use to build this tool?",
            "_A104":"Bootstrap, Handsontable.js and dataframe.js.",
        }


d_static = {
        "current_year": date.today().year,
        "url_index": "index.html",
        "url_blog": "blog/index.html",
    }


d_websites=[
    {
        "blog_url": "careercrashcourse.com",
        "blog_logo": "CareerCrashCourse",
        "title": "CareerCrashCourse",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "blog/index.html",
         nav:[{"nav_text":"Blog","nav_url": "blog/index.html"},]
    },
    {
        "blog_url": "shoulderofgiants.com",
        "blog_logo": "Shoulder of Giants",
        "title": "ShoulderofGiants",
        "lang": "en",
        "metadescription": "A collection of spreadsheet tools online. Each tool is specifically design to solve one spreadsheet problem.",
        "metakeywords": "Online, Spreadsheet, Micro Saas",
        "redirect": "blog/index.html",
        nav:[{"nav_text":"Blog","nav_url": "blog/index.html"},]
    },
    {
        "blog_url": "sicksheet.com",
        "blog_logo": "SICK.SHEET",
        "title": "SickSheet",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "tools/index.html",
        nav:[{"nav_text":"Tools","nav_url": "tools/index.html"},
             {"nav_text":"Blog","nav_url": "blog/index.html"},]
    }]



