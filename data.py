from datetime import *
from function import get, pformat
import function
"""
blog data are stored in word files
tool data are stored in dict/obj
website meta data are stored in dict
"""

#same for all tools, g for general
d_tools_txt_g={
    "input.title":"Input",
    "input.descr":"Copy paste your table here.",
    "input.content":"",
    "configure.title":"Configure",
    "configure.descr":"Configure the options.",
    "configure.content":"",
    "download.title":"Download",
    "download.descr":"Copy or Download your result in CSV.",
    "download.content":"",
}

#s for specific. specific tool dict
d_tools_txt_s=[
    {
        "tool":"join-tables",
        "h1":"Join Tables",
        "h1description": "Merge and join two spreadsheets based on their key column.",
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
        "input.title" :"Input Right Table",
        "input.descr" :"Paste in your right table here.",
        "input2.title" :"Input Left Table",
        "input2.descr" :"Paste in your left table here.",
    },

    {
        "tool":"transpose-table",
        "h1":"Transpose Table",
        "h1description": "Swap spreadsheet column and row axis.",
        "metakeywords": "Online, Spreadsheet, Transpose",
    },

    {
        "tool":"sort-rows",
        "h1":"Sort Tables",
        "h1description": "Sort spreadsheet columns in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Sort",
    },

    {
        "tool": "first-n-rows",
        "h1": "First n Rows",
        "h1description": "Get the first n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Head, first row",
        "configure.content": "First n Rows",
    },


    {
        "tool":"last-n-rows",
        "h1":"Last n Rows",
        "h1description": "Get the last n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Tail, last row",
    },


    {
        "tool":"sample-rows",
        "h1":"Get Sample Rows",
        "h1description": "Get a sampled subset of rows in a spreadsheet",
        "metakeywords": "Online, Spreadsheet, Sample, Subset",
        "configure.content": "Sample n Percent",
    },


    {
        "tool": "slice-rows",
        "h1": "Slice Rows",
        "h1description": "Get a subset of Consecutive Rows.",
        "metakeywords": "Online, Spreadsheet, Slice",
        "configure.content": "Start from Row n",
    },



       {
        "tool":"shuffle-rows",
        "h1":"Shuffle Table Rows",
        "h1description": "Randomly shuffle rows of your spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Shuffle, Random",
        "configure.content": "Shuffle Row",
    },


    {
        "tool":"drop-duplicated-columns",
        "h1":"Drop Duplicated Columns",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Drop Duplicates, Remove Duplicates",
    },
]


#same for all faq tools
d_tools_faq_g={
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


#same for all blogs
d_websites_g = {
        "current_year": date.today().year,
        "url_index": "index.html",
        "url_blog": "blog/index.html",
    }


#same for all websites
d_websites_s=[
    {
        "blog_url": "careercrashcourse.com",
        "blog_logo": "CareerCrashCourse",
        "title": "CareerCrashCourse",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "blog/index.html",
         function.nav:[{"nav_text": "Blog", "nav_url": "blog/index.html"}, ]
    },
    {
        "blog_url": "shoulderofgiants.com",
        "blog_logo": "Shoulder of Giants",
        "title": "ShoulderofGiants",
        "lang": "en",
        "metadescription": "A collection of spreadsheet tools online. Each tool is specifically design to solve one spreadsheet problem.",
        "metakeywords": "Online, Spreadsheet, Micro Saas",
        "redirect": "blog/index.html",
        function.nav:[{"nav_text": "Blog", "nav_url": "blog/index.html"}, ]
    },
    {
        "blog_url": "sicksheet.com",
        "blog_logo": "SICK.SHEET",
        "title": "SickSheet",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "tools/index.html",
        function.nav:[{"nav_text": "Tools", "nav_url": "tools/index.html"},
                      {"nav_text":"Blog","nav_url": "blog/index.html"}, ]
    }]



