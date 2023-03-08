from datetime import *

import function

"""
blog data are stored in word files
tool data are stored in dict/obj
website meta data are stored in dict
"""

# same for all tools, g for general
d_tools_txt_g = {
    "input.title": "Input",
    "input.descr": "Copy paste your table here.",
    "input.content": "",
    "configure.title": "Configure",
    "configure.descr": "Configure the options.",
    "configure.content": "",
    "download.title": "Download",
    "download.descr": "Copy or Download your result in CSV.",
    "download.content": "",
}

d_tools_filter = [
    {
        "tool": "first-n-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "First n Rows",
        "h1description": "Get the first n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Head, first row, starting line, start series",
        "configure.content": "First n Rows",
    },
    {
        "tool": "last-n-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Last n Rows",
        "h1description": "Get the last n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Tail, last row, ending line, end series",
    },
    {
        "tool": "after-first-n-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "After First n Rows",
        "h1description": "Skip the first n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, first row, skip first n rows, after n rows",
        "configure.content": "First n Rows",
    },

    {
        "tool": "before-last-n-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Before Last n Rows",
        "h1description": "Skip the last n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, before last row, skip last n rows, before last n rows",
    },

    {
        "tool": "slice-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Rows Between",
        "h1description": "Get a subset of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Slice, Between, from row n to m",
        "configure.content": "Start from Row n",
    },

    {
        "tool": "sample-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Get Sample Rows",
        "h1description": "Randomly Sample rows of a spreadsheet",
        "metakeywords": "Online, Spreadsheet, Table, Sample, Subset, Random Sample, Select Random Rows",
        "configure.content": "Sample n Percent",
    },

    {
        "tool": "shuffle-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Shuffle Table Rows",
        "h1description": "Randomly shuffle rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Shuffle, Random, Mix Rows, Mix Table",
        "configure.content": "Shuffle Row",
    },

    {
        "tool": "even-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Get Even Rows",
        "h1description": "Get even rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Even Rows, Skip every second Row ",
    },

    {
        "tool": "odd-rows",
        "args": ["table"],
        "type": "filter",
        "h1": "Get Odd Rows",
        "h1description": "Get odd rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Odd Rows, Skip odd rows",
    },

    {
        "tool": "nth-row",
        "args": ["table"],
        "type": "filter",
        "h1": "Every nth Row",
        "h1description": "Get every nth rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Get every nth row.",
    },

    {
        "tool": "except-nth-row",
        "args": ["table"],
        "type": "filter",
        "h1": "Except nth Row",
        "h1description": "Get the spreadsheet except every nth row.",
        "metakeywords": "Online, Spreadsheet, Table, Skip every nth Row",
    },

    {
        "tool": "text-len",
        "args": ["table"],
        "type": "filter",
        "h1": "Text Length",
        "h1description": "Count the text length of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Length of every text, text length",
    },

    {
        "tool": "char-to-number",
        "args": ["table"],
        "type": "filter",
        "h1": "Character to Number",
        "h1description": "Convert English Character to number. a = 1, b = 2 ... z = 26. ",
        "metakeywords": "Online, Spreadsheet, Table, Alphabet to number",
    },

    {
        "tool": "number-to-char",
        "args": ["table"],
        "type": "filter",
        "h1": "Conver numbers to English Character. 1 = a, 2 = b, 3 = c, ... 26 = z.",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Table, Number to Alphabet",
    },

]

d_tools_text = [

    {
        "tool": "remove-leading-space",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Remove Leading Space",
        "h1description": "Remove starting spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Space",
    },

    {
        "tool": "remove-trailing-space",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Remove Trailing Space",
        "h1description": "Remove ending spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Ending Space",
    },

    {
        "tool": "trim-space",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Remove Leading & Trailing Space",
        "h1description": "Remove starting and ending spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Space, Remove Ending Space",
    },

    {
        "tool": "replace-space",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Replace Space",
        "h1description": "Replace space with another delimiter.",
        "metakeywords": "Online, Spreadsheet, Table, Replace Space with, Replace space with comma, Replace space with hyphen",
    },

    {
        "tool": "capitalize",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Capitalize Sentence",
        "h1description": "Uppercase each starting letter of a sentence.",
        "metakeywords": "Online, Spreadsheet, Table, Title Case, Capital Case, Upper Case",
    },

    {
        "tool": "proper",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Capitalize Every Word",
        "h1description": "Upper case each starting letter of a word.",
        "metakeywords": "Online, Spreadsheet, Table, Capital case for each word, Title case for each word",
    },

    {
        "tool": "upper",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Uppercase Text",
        "h1description": "Upper case everything in the spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Upper case, Capital letters",
    },

    {
        "tool": "lower",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Lowercase Text",
        "h1description": "Lower case everything in the spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Lower Case, Lower letters",
    },
    {
        "tool": "left",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Left of Text",
        "h1description": "Get the left n characters of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Get left n characters, cut, separate left text part",
    },

    {
        "tool": "right",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Right of Text",
        "h1description": "Get the right n characters of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Get right n characters, cut, separate right text part",
    },
    {
        "tool": "join-text",
        "args": ["table"],
        "type": "text-mod",
        "h1": "Join Text Together",
        "h1description": "Combine each cell together to one cell.",
        "metakeywords": "Online, Spreadsheet, Table, Combine each row together, combine text",
    },

]

d_tools_math = [

    {
        "tool": "add-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Add Tables",
        "h1description": "Add two spreadsheets together.",
        "metakeywords": "Online, Spreadsheet, Table, Addition, Add, Combine, Plus",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },

    {
        "tool": "subtract-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Subtract Tables",
        "h1description": "Subtract 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Subtraction, Minus",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },

    {
        "tool": "multiply-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Multiply Tables",
        "h1description": "Multiply 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Multiplication, Times",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },

    {
        "tool": "divide-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Divide Tables",
        "h1description": "Divide the data of 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Division, Divide",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },
    {
        "tool": "exponent-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Power Tables",
        "h1description": "Spreadsheet 1 acts as basis, spreadsheet 2 acts as exponent. ",
        "metakeywords": "Online, Spreadsheet, Table, Addition, Exponential, Base, Exponent",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },
    {
        "tool": "dot-product-tables",
        "args": ["table", "table"],
        "type": "math",
        "h1": "Dot Product Tables",
        "h1description": "Scalar product the data of 2 tables into a new table.",
        "metakeywords": "Online, Spreadsheet, Table, Scalar Product, Dot Product, Matrix Product",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },

    {
        "tool": "abs-values",
        "args": ["table"],
        "type": "math",
        "h1": "Absolute Values",
        "h1description": "Turn negative values into positive values.",
        "metakeywords": "Online, Spreadsheet, Table, Absolute value, Negative to positive values",
    },

    {
        "tool": "round-values",
        "args": ["table"],
        "type": "math",
        "h1": "Round Values",
        "h1description": "Round each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Numbers",
    },
    {
        "tool": "round-up",
        "args": ["table"],
        "type": "math",
        "h1": "Round Up",
        "h1description": "Round up each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Up, Ceiling Function",
    },

    {
        "tool": "round-down",
        "args": ["table"],
        "type": "math",
        "h1": "Round Down",
        "h1description": "Round down each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Down, Floor Function",
    },

    {
        "tool": "rank-table",
        "args": ["table"],
        "type": "math",
        "h1": "Rank Table",
        "h1description": "Rank each number of a spreadsheet in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Rank",
    },

    {
        "tool": "percentile-table",
        "args": ["table"],
        "type": "math",
        "h1": "Percentile Table",
        "h1description": "Pertent Rank each number of a spreadsheet in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Rank Percent",
    },

    {
        "tool": "add-leading-zeros",
        "args": ["table"],
        "type": "math",
        "h1": "Add Leading Zeros",
        "h1description": "Add starting zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Add Start Zero, Begin Zeros",
    },

    {
        "tool": "add-trailing-zeros",
        "args": ["table"],
        "type": "math",
        "h1": "Add Trailing Zeros",
        "h1description": "Add ending zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Add Ending Zero, End zero",
    },

    {
        "tool": "remove-leading-zeros",
        "args": ["table"],
        "type": "math",
        "h1": "Remove Leading Zeros",
        "h1description": "Remove starting zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Zero, drop first zero",
    },

    {
        "tool": "remove-trailing-zeros",
        "args": ["table"],
        "type": "math",
        "h1": "Remove Trailing Zeros",
        "h1description": "Remove ending zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Ending Zero, drop last zero",
    },

    {
        "tool": "sum",
        "args": ["table"],
        "type": "math",
        "h1": "Sum of Columns",
        "h1description": "Calculate the sum of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Summation of column",
    },

    {
        "tool": "average",
        "args": ["table"],
        "type": "math",
        "h1": "Average of Columns",
        "h1description": "Calculate the average of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Average of column",
    },

    {
        "tool": "min",
        "args": ["table"],
        "type": "math",
        "h1": "Minimum of Columns",
        "h1description": "Calculate the minimum number of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Minimum of column",
    },

    {
        "tool": "max",
        "args": ["table"],
        "type": "math",
        "h1": "Maximum of Columns",
        "h1description": "Calculate the maximum number of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Maximum of column",
    },
    {
        "tool": "random-table",
        "args": ["table"],
        "type": "math",
        "h1": "Fill Random Number",
        "h1description": "Create a spreadsheet filled with random numbers.",
        "metakeywords": "Online, Spreadsheet, Table, Fill Numbers, Random Numbers",
    },
]

d_tools_database = [
    {
        "tool": "join-tables",
        "args": ["table", "table"],
        "type": "database",
        "h1": "Join Tables",
        "h1description": "Merge two spreadsheets based on their key columns.",
        "metakeywords": "Online, Spreadsheet, Table, Join, Merge, Concat",
        "_Q1": "What is the difference between Left Join, Right Join, Inner Join and Outer Join?",
        "_A1": """<ul>
          <li><b>Inner Join</b>: Returns records that have matching values in <b>both tables</b></li>
          <li><b>Left (Outer) Join</b>: Returns all records from the <b>left table</b>, and the matched records from the right table</li>
          <li><b>Right (Outer) Join</b>: Returns all records from the <b>right table</b>, and the matched records from the left table</li>
          <li><b>Full (Outer) Join</b>: Returns all records when there is a match in <b>either left or right table</b></li>
        </ul>""",
        "_Q2": "I uploaded both sheets, but it doesn't produce results.",
        "_A2": "A: Make sure the key of each sheet is in the first column and that they are named <b>exactly the same</b>. You can edit the column name in the online table directly.",
        "input.title": "Input Right Table",
        "input.descr": "Paste in your right table here.",
        "input2.title": "Input Left Table",
        "input2.descr": "Paste in your left table here.",
    },

    {
        "tool": "transpose-table",
        "args": ["table"],
        "type": "database",
        "h1": "Transpose Table",
        "h1description": "Swap spreadsheet column and row axis.",
        "metakeywords": "Online, Spreadsheet, Table, Transpose, Change Axis, Swap Orientation",
    },

    {
        "tool": "sort-rows",
        "args": ["table"],
        "type": "database",
        "h1": "Sort Tables",
        "h1description": "Sort spreadsheet rows in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Sort Rows, Sort Tables",
    },

    {
        "tool": "unique-values",
        "args": ["table"],
        "type": "database",
        "h1": "Unique Values",
        "h1description": "A Filter that only shows unique values of each columns.",
        "metakeywords": "Online, Spreadsheet, Table, Unique, Distinct, No Duplicate",
    },

    {
        "tool": "group-by",
        "args": ["table"],
        "type": "database",
        "h1": "Group By Column",
        "h1description": "Group the entire spreadsheet by a desired column.",
        "metakeywords": "Online, Spreadsheet, Table, Group By, Grouping",
    },

    {
        "tool": "drop-duplicated-columns",
        "args": ["table"],
        "type": "database",
        "h1": "Drop Duplicated Columns",
        "h1description": "Remove columns with the same name.",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
    },

]

d_tools_converter = [

    {
        "tool": "to-dsv",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to DSV",
        "h1description": "Save Spreadsheet as Delimiter Separated Values (dsv).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to DSV, Delimiter",
    },

    {
        "tool": "to-csv",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to CSV",
        "h1description": "Save Spreadsheet as Comma Separated Values (dsv).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to CSV, Comma",
    },

    {
        "tool": "to-json",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to JSON",
        "h1description": "Save Spreadsheet as JavaScript Object Notation (json).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to JSON, javascript object",
    },

    {
        "tool": "to-dict",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to Dictionary",
        "h1description": "Save Spreadsheet as Dictionary.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to Dictionary, Dict",
    },

    {
        "tool": "to-array",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to array",
        "h1description": "Save Spreadsheet as Array.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to array",
    },

    {
        "tool": "to-collection",
        "args": ["table"],
        "type": "converter",
        "h1": "Table to collection",
        "h1description": "Save Spreadsheet as collection.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to collection",
    },

    {
        "tool": "from-csv",
        "args": ["table"],
        "type": "converter",
        "h1": "CSV to Table",
        "h1description": "Paste in CSV files to create a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Convert from CSV, Comma",
    },

]

# s for specific. specific tool dict
d_tools_txt_s = d_tools_filter + d_tools_text + d_tools_math + d_tools_database + d_tools_converter

# same for all faq tools
d_tools_faq_g = {
    "_Q100": "Can I upload my data as .xlsx or .csv file?",
    "_A100": "Upload data as .xlsx or .csv file is not supported yet. You can copy paste your data from excel into the website table above.",
    "_Q101": "Can it handle big data sets?",
    "_A101": "Upload data as .xlsx or .csv file is not supported yet.   A: Yes it can handle tables up to 6000 columns and rows. If you encounter lag, you can reduce the sheet size.",
    "_Q102": "It is normal that it lags a couple of seconds during copy paste?",
    "_A102": "Yes this is normal for a web based application (especially when the data set is large).",
    "_Q103": "The provided spreadsheet interface is very small. Can you make it bigger?",
    "_A103": "It is recommended to paste data into Excel to manage a bigger data sets.",
    "_Q104": "What plugin do you use to build this tool?",
    "_A104": "Bootstrap, Handsontable.js and dataframe.js.",
}

# same for all blogs
d_websites_g = {
    "current_year": date.today().year,
    "url_index": "index.html",
    "url_blog": "blog/index.html",
}

# same for all websites
d_websites_s = [
    {
        "blog_url": "careercrashcourse.com",
        "blog_logo": "CareerCrashCourse",
        "title": "CareerCrashCourse",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "blog/index.html",
        function.nav: [{"nav_text": "Blog", "nav_url": "blog/index.html"}, ]
    },
    {
        "blog_url": "shoulderofgiants.com",
        "blog_logo": "Shoulder of Giants",
        "title": "ShoulderofGiants",
        "lang": "en",
        "metadescription": "A collection of spreadsheet tools online. Each tool is specifically design to solve one spreadsheet problem.",
        "metakeywords": "Online, Spreadsheet, Table, Micro Saas",
        "redirect": "blog/index.html",
        function.nav: [{"nav_text": "Blog", "nav_url": "blog/index.html"}, ]
    },
    {
        "blog_url": "sicksheet.com",
        "blog_logo": "SICK.SHEET",
        "title": "SickSheet",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "tools/index.html",
        function.nav: [{"nav_text": "Tools", "nav_url": "tools/index.html"},
                       {"nav_text": "Blog", "nav_url": "blog/index.html"}, ]
    }]

"""

{
        "tool":"from-json",
        "h1":"From JSON to Spreadsheet",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
    },

    {
        "tool":"from-dict",
        "h1":"From Dictionary to Spreadsheet",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
    },

    {
        "tool":"from-array",
        "h1":"From Array to Spreadsheet",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
    },

    {
        "tool":"from-collection",
        "h1":"From Collection to collection",
        "h1description": "Remove columns with the same name",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
    },

"""
