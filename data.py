from datetime import *
from main import get,pformat
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


def tool_steps(tooldata,d_website):
    result=""
    for counter, d_step in enumerate(tooldata):
        onestep=get("component_tool_step.html").format(**{
            "stepnumber":counter+1,
            "steptitle": d_step["steptitle"],
            "stepdescription":d_step["stepdescription"],
            "stepcontent":d_step["stepcontent"],
        })
        result+=onestep
    result = pformat(result, d_website)
    return result



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



d_tools={
    "join":{
        "tool":"join",
        "h1":"Join Tables",
        "h1description": "Merge and join Excel sheets directly online in just 3 steps.",
        "title": "Join Table Online",
        "metadescription": "An free online too to join spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Join, Merge",
        tool_faq:{
            "Q: What is the difference between Left Join, Right Join, Inner Join and Outer Join?":"""A:
        <ul>
          <li><b>Inner Join</b>: Returns records that have matching values in <b>both tables</b></li>
          <li><b>Left (Outer) Join</b>: Returns all records from the <b>left table</b>, and the matched records from the right table</li>
          <li><b>Right (Outer) Join</b>: Returns all records from the <b>right table</b>, and the matched records from the left table</li>
          <li><b>Full (Outer) Join</b>: Returns all records when there is a match in <b>either left or right table</b></li>
        </ul>""",
            "Q: I uploaded both sheets, but it doesn't produce results.": "A: Make sure the key of each sheet is in the first column and that they are named <b>exactly the same</b>. You can edit the column name in the online table directly.",
        },
        tool_steps:[
            {"steptitle":"Input Left Table",
             "stepdescription":"Copy paste your first table here.",
             "stepcontent":'<div id="table1"></div>',
             },
             {"steptitle":"Input Right Table",
              "stepdescription":"Copy paste your second table here.",
              "stepcontent":'<div id="table2"></div><div id="leftalert" class="alert alert-danger" role="alert" style="display:none;"></div>',
              },
             {"steptitle":"Choose Join Type",
              "stepdescription":"Choose the Join type.",
              "stepcontent":"""<select id="jointype" class="form-select width50" style="display:inline-block;width:100%;margin:0px;" >
                                  <option value="left" selected>Left Join</option>
                                  <option value="right">Right Join</option>
                                  <option value="inner">Inner Join</option>
                                  <option value="outer">Outer Join</option>
                                </select>
                            <img id="joinimg" alt="Join type image as Venn Diagram" src="" loading="lazy" width="350" height="190" >
                        """,
              },
             {"steptitle":"Download Joined Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table3"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
    },


    "transpose":{
        "tool":"transpose",
        "h1":"Transpose Tables",
        "h1description": "Transpose Excel sheets directly online.",
        "title": "Transpose Table Online",
        "metadescription": "An free online too to transpose spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Transpose",
        tool_faq:{},
        tool_steps:[
            {"steptitle":"Input Table",
             "stepdescription":"Copy paste your table here.",
             "stepcontent":'<div id="table1"></div>',
             },
             {"steptitle":"Download Transposed Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table2"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
    },


    "sort":{
        "tool":"sort",
        "h1":"Sort Tables",
        "h1description": "Sort Excel sheets directly online.",
        "title": "Sort Table Online",
        "metadescription": "An free online too to sort spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Sort",
        tool_faq:{},
        tool_steps:[
            {"steptitle":"Input Table",
             "stepdescription":"Copy paste your table here.",
             "stepcontent":'<div id="table1"></div>',
             },
            {"steptitle":"Select Option",
             "stepdescription":"Select sorting column and type",
             "stepcontent":"""<select id="sortcol" class="form-select width50" style="display:inline-block;width:100%;margin:0px;" >
                                </select>
                            <select id="asc" class="form-select width50" style="display:inline-block;width:100%;margin:0px;" >
                                <option value=true >Ascending</option>
                                <option value=false >Descending</option>
                            </select>
                        """,
             },
             {"steptitle":"Download Sorted Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table2"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
    },

    "tail":{
        "tool":"tail",
        "h1":"Last n Rows",
        "h1description": "Get the last n rows of an Excel sheets directly online.",
        "title": "Get Last n Rows Online",
        "metadescription": "An free online too to get the last n rows of a spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Tail, last row",
        tool_faq:{},
        tool_steps:[
            {"steptitle":"Input Table",
             "stepdescription":"Copy paste your table here.",
             "stepcontent":'<div id="table1"></div>',
             },
            {"steptitle":"Select Option",
             "stepdescription":"Select sorting column and type",
             "stepcontent":"""<input id="n" type="range" class="form-range" min="1" max="100">
                        """,
             },
             {"steptitle":"Download Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table2"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
    },
}




d_general_faq={
            "Q: Can I upload my data as .xlsx or .csv file?":"A: Upload data as .xlsx or .csv file is not supported yet. You can copy paste your data from excel into the website table above.",
            "Q: Can it handle big data sets?":"A: Upload data as .xlsx or .csv file is not supported yet.   A: Yes it can handle tables up to 6000 columns and rows. If you encounter lag, you can reduce the sheet size.",
            "Q: It is normal that it lags a couple of seconds during copy paste?": "A: Yes this is normal for a web based application (especially when the data set is large).",
            "Q: The provided spreadsheet interface is very small. Can you make it bigger?": "A: It is recommended to paste data into Excel to manage a bigger data sets.",
            "Q: What plugin do you use to build this tool?": "A: Bootstrap, Handsontable.js and dataframe.js.",
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



