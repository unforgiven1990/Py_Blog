
"""
blog data are stored in word files
tool data are stored in dict/obj
website meta data are stored in dict
"""


data_tool={
    "join":{
        "h1":"Join Tables Online",
        "h1description": "Merge and join Excel sheets directly online in just 3 steps.",
        "title": "Join Table Online • {blog_url}",
        "metadescription": "An free online too to join spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Join, Merge",
        "QA":{
            "Q: What is the difference between Left Join, Right Join, Inner Join and Outer Join?":"""A:
        <ul>
          <li><b>Inner Join</b>: Returns records that have matching values in <b>both tables</b></li>
          <li><b>Left (Outer) Join</b>: Returns all records from the <b>left table</b>, and the matched records from the right table</li>
          <li><b>Right (Outer) Join</b>: Returns all records from the <b>right table</b>, and the matched records from the left table</li>
          <li><b>Full (Outer) Join</b>: Returns all records when there is a match in <b>either left or right table</b></li>
        </ul>""",
            "Q: I uploaded both sheets, but it doesn't produce results.": "A: Make sure the key of each sheet is in the first column and that they are named <b>exactly the same</b>. You can edit the column name in the online table directly.",
        },
        "toolsteps":[
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
             {"steptitle":"Download Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table3"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
        "js":"",
        "css":"",
    },


    "transpose":{
        "h1":"Transpose Tables Online",
        "h1description": "Transpose Excel sheets directly online.",
        "title": "Transpose Table Online • {blog_url}",
        "metadescription": "An free online too to transpose spreadsheets online. Easy to use and completely free. No login required.",
        "metakeywords": "Online, Spreadsheet, Transpose",
        "QA":{},
        "toolsteps":[
            {"steptitle":"Input Left Table",
             "stepdescription":"Copy paste your first table here.",
             "stepcontent":'<div id="table1"></div>',
             },
             {"steptitle":"Input Right Table",
              "stepdescription":"Copy paste your second table here.",
              "stepcontent":'<div id="table2"></div>',
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
             {"steptitle":"Download Result",
              "stepdescription":"Copy or Download your result in CSV.",
              "stepcontent":'<div id="table3"></div><button id="download" type="button" class="btn btn-primary width50" style="display:inline-block;width:100%;margin:0px;" > Download</button>',
              },
        ],
        "js": "",
        "css": "",
    }
}




data_general_AQ={
            "Q: Can I upload my data as .xlsx or .csv file?":"A: Upload data as .xlsx or .csv file is not supported yet. You can copy paste your data from excel into the website table above.",
            "Q: Can it handle big data sets?":"A: Upload data as .xlsx or .csv file is not supported yet.   A: Yes it can handle tables up to 6000 columns and rows. If you encounter lag, you can reduce the sheet size.",
            "Q: It is normal that it lags a couple of seconds during copy paste?": "A: Yes this is normal for a web based application (especially when the data set is large).",
            "Q: The provided spreadsheet interface is very small. Can you make it bigger?": "A: It is recommended to paste data into Excel to manage a bigger data sets.",
            "Q: What plugin do you use to build this tool?": "A: Bootstrap, Handsontable.js and dataframe.js.",
        }




data_websites=[
    {
        "blog_url": "careercrashcourse.com",
        "blog_logo": "CareerCrashCourse",
        "blog_normal": "CareerCrashCourse",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
    },
    {
        "blog_url": "shoulderofgiants.com",
        "blog_logo": "Shoulder of Giants",
        "blog_normal": "ShoulderofGiants",
        "lang": "en",
        "metadescription": "A collection of spreadsheet tools online. Each tool is specifically design to solve one spreadsheet problem.",
        "metakeywords": "Online, Spreadsheet, Micro Saas",
    },
    {
        "blog_url": "sicksheet.com",
        "blog_logo": "SickSheet",
        "blog_normal": "SickSheet",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
    }]


