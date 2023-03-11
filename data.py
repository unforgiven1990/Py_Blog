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
        "complexity": "simple",
        "h1": "First n Rows",
        "h1description": "Get the first n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Head, first row, starting line, start series",
        "configure.content": "First n Rows",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives the first n rows of your tables. For example, it gives you the first 10 rows of a huge table.",
        "_Q2": "When is it useful?",
        "_A2": "If you have a messy dataset and you want to only select a small sample of the data to play around with. If your PC is laging due to the big datasize, you should reduce the table size as well.",
    },
    {
        "tool": "last-n-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Last n Rows",
        "h1description": "Get the last n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Tail, last row, ending line, end series",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives the last n rows of your tables. For example, it gives you the last 10 rows of a huge table.",
        "_Q2": "When is it useful?",
        "_A2": "If your dataset is too big or if your last rows are more important than the other dataset. After filtering, you can calculate sum and average of the selected subset.",

    },
    {
        "tool": "after-first-n-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "After First n Rows",
        "h1description": "Skip the first n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, first row, skip first n rows, after n rows",
        "configure.content": "After n Rows",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives the a new table that skips the first n rows. For example, your table has 100 rows. You skip the first 10, and the get a new table from row 11-100.",
        "_Q2": "When is it useful?",
        "_A2": "If the first n rows contain junk information that you want to skip. If your data is too big to operate and you want to reduce the size. If you want to calculate the average of a subset but not the entire table.",

    },

    {
        "tool": "before-last-n-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Before Last n Rows",
        "h1description": "Skip the last n rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, before last row, skip last n rows, before last n rows",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It skippes the last n rows of your table. For example, your table has 100 rows, it deletes the last 10 rows and gives you the row 1-90.",
        "_Q2": "When is it useful?",
        "_A2": "If your dataset is too big or if your last rows are irrelevant dataset. After filtering, you can calculate sum and average of the selected subset.",

    },

    {
        "tool": "slice-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Rows Between",
        "h1description": "Get a subset of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Slice, Between, from row n to m",
        "configure.content": "Start from Row n",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives the middle of a table. For example, you have a table of 100 rows. The tool gives you a new table from row 33-66.",
        "_Q2": "When is it useful?",
        "_A2": "If your dataset is too big or if only selected middle rows are important. After filtering, you can calculate sum and average of the selected subset.",

    },

    {
        "tool": "sample-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Get Sample Rows",
        "h1description": "Randomly Sample rows of a spreadsheet",
        "metakeywords": "Online, Spreadsheet, Table, Sample, Subset, Random Sample, Select Random Rows",
        "configure.content": "Sample n Percent",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It randomly selects rows of your table. For example, your table has 100 rows, the tool randomly picks row 4,55,and 78 to create a new table.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to select some data to validate or to check the quality. If you have a table of test questions and you want to pick some questions to ask your students.",

    },

    {
        "tool": "shuffle-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Shuffle Table Rows",
        "h1description": "Randomly shuffle rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Shuffle, Random, Mix Rows, Mix Table",
        "configure.content": "Shuffle Row",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It changes the row order of your table in a random manner.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to keep the dataset in a desired order. If you want to disorder the data to conceive information for the viewer.",

    },

    {
        "tool": "even-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Get Even Rows",
        "h1description": "Get even rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Even Rows, Skip every second Row ",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives every even row of the table. For example, it gives you row 2,4,6,8,...",
        "_Q2": "When is it useful?",
        "_A2": "If your table is missformated and all the data are in every second row. If your table is designed in a way that every second row are correclated and you want to split the table.",

    },

    {
        "tool": "odd-rows",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Get Odd Rows",
        "h1description": "Get odd rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Odd Rows, Skip odd rows",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives every odd row of the table. For example, it gives you row 1,3,5,9,...",
        "_Q2": "When is it useful?",
        "_A2": "If your table is missformated and all the data are in every second row. If your table is designed in a way that every second row are correclated and you want to split the table.",
    },

    {
        "tool": "text-len",
        "args": ["table"],
        "type": "filter",
        "complexity": "simple",
        "h1": "Text Length",
        "h1description": "Count the text length of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Length of every text, text length",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": 'It gives a new table that calculates the text length for each cell. For example, the word "abc" would have the length 3.',
        "_Q2": "When is it useful?",
        "_A2": "If you want to find out which cell is the longest. If you want to find out the average text length of your data.",
    },

    {
        "tool": "nth-row",
        "args": ["table"],
        "type": "filter",
        "complexity": "advanced",
        "h1": "Every nth Row",
        "h1description": "Get every nth rows of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Get every nth row.",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It gives a new table containing every nth row of the input table. For example, the new table contains every 3rd row.",
        "_Q2": "When is it useful?",
        "_A2": "If your table is structured in a particular way that all relevant information are stored in every nth row. Selecting them in this way allows easier access to the data.",
    },

    {
        "tool": "except-nth-row",
        "args": ["table"],
        "type": "filter",
        "complexity": "advanced",
        "h1": "Except Every nth Row",
        "h1description": "Get the spreadsheet except every nth row.",
        "metakeywords": "Online, Spreadsheet, Table, Skip every nth Row",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It deletes every nth row of the input table. For example, it gives you a new table without row 3,6,9,12,...",
        "_Q2": "When is it useful?",
        "_A2": "If your table is structured in a way that some rows are irrelevant and can be deleted. Deleting these rows will result in a cleaner dataset.",
    },

    {
        "tool": "char-to-number",
        "args": ["table"],
        "type": "filter",
        "complexity": "advanced",
        "h1": "Character to Number",
        "h1description": "Convert English Character to number. a = 1, b = 2 ... z = 26. ",
        "metakeywords": "Online, Spreadsheet, Table, Alphabet to number",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a character into number. For example a converts to 1, and z converts to 26.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to change who the data is represented. After converting the character into numbers, you can do mathematical calculations on them (such as +, -, *, %).",

    },

    {
        "tool": "number-to-char",
        "args": ["table"],
        "type": "filter",
        "complexity": "advanced",
        "h1": "Number to Character",
        "h1description": "Convert numbers to English Character. 1 = a, 2 = b, 3 = c, ... 26 = z.",
        "metakeywords": "Online, Spreadsheet, Table, Number to Alphabet",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts any number into a character. For example, 1 = a, 2 = b, 3 = c, ... 26 = z.",
        "_Q2": "When is it useful?",
        "_A2": "If you already are using number as another identifiers (column index or row index), then it is better to use another non-numeric index.",

    },

]

d_tools_text = [

    {
        "tool": "remove-leading-space",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Remove Leading Space",
        "h1description": "Remove starting spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Space",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It removes any white space character in front of your actual table content. For example, the word ' hello', will be convert to 'hello'. ",
        "_Q2": "When is it useful?",
        "_A2": "If you copy paste a table, white space character often appears before the first actual letter. It is good to remove them in order to clean up your data.",

    },

    {
        "tool": "remove-trailing-space",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Remove Trailing Space",
        "h1description": "Remove ending spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Ending Space",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It removes any white space character at the end of each cell. For example, the word 'hello ', will be convert to 'hello'. ",
        "_Q2": "When is it useful?",
        "_A2": "If your table is manually created, sometimes people include unessesary whitespace. It is good to remove them in order to clean up your data.",

    },

    {
        "tool": "trim-space",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Remove Leading & Trailing Space",
        "h1description": "Remove starting and ending spaces.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Space, Remove Ending Space",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It removes any white space character at the start and end of your cell. For example, the word ' hello world ', will be convert to 'hello world'. ",
        "_Q2": "When is it useful?",
        "_A2": "It is good to remove them in order to clean up your data. Some copy pasted tables include unessesary white space.",

    },

    {
        "tool": "replace-space",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Replace Space",
        "h1description": "Replace space with another delimiter.",
        "metakeywords": "Online, Spreadsheet, Table, Replace Space with, Replace space with comma, Replace space with hyphen",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It replaces all space characters with another symbol. For example, the word 'hello', will be convert to 'hello,' whereas space is replaced with comma. You can choose any other symbols to replace the space characer. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains unessesary space characters and you want to consolidate them. If you want to give more meaning to your data by using another symbol tha the space sign.",

    },

    {
        "tool": "capitalize",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Capitalize Sentence",
        "h1description": "Uppercase each starting letter of a sentence.",
        "metakeywords": "Online, Spreadsheet, Table, Title Case, Sentence Case, Capital Case, Upper Case",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It turns every first letter of a cell into capital letter. For example, the word 'hello you', will be convert to 'Hello you'. It convert following words and only converts the first letter into capital case.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to write in title case (for page title, powerpoint slide title, article title) to emphasize on the title content.",

    },

    {
        "tool": "proper",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Capitalize Every Word",
        "h1description": "Upper case each starting letter of a word.",
        "metakeywords": "Online, Spreadsheet, Table, Capital case for each word, Title case for each word",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It turns All words to capital case. For example, the word 'have a nice day', will be convert to 'Have A Nice Day'.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to write in title case (for page title, powerpoint slide title, article title) to emphasize on the title content.",

    },

    {
        "tool": "upper",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Uppercase Text",
        "h1description": "Upper case everything in the spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Upper case, Capital letters",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It turns all letters of a cell into upper case. For example, the word 'hello you', will be convert to 'HELLO YOU'.",
        "_Q2": "When is it useful?",
        "_A2": "Usually all company logo or branded words can be written in capital letters. Or if you want to emphasize on a particular data and make it all capital case.",

    },

    {
        "tool": "lower",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Lowercase Text",
        "h1description": "Lower case everything in the spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Lower Case, Lower letters",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It turns every first letter of a cell into lower case. For example, the word 'Hello You', will be convert to 'hello you'.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to write in bullet points it is recommended to write in lower case. If you want to make more text to lower case so that your capital cased words truly stand out.",

    },
    {
        "tool": "left",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Left-Pad Text",
        "h1description": "Get the left n characters of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Pad, Get left n characters, cut, separate left text part",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It gives a part of each cell data by start counting from left to right. For example 'hello world' can be turned into 'hello' if choosing the number 5 in the configurator. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data is ordered in a way that only the first n letters are meaningful. If you want to reduce the general length of your data and make it more compact.",

    },

    {
        "tool": "right",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Right-Pad Text",
        "h1description": "Get the right n characters of each cell.",
        "metakeywords": "Online, Spreadsheet, Table, Pad, Get right n characters, cut, separate right text part",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It gives a part of each cell data by start counting from right to left. For example 'hello world' can be turned into 'world' if choosing the number 5 in the configurator. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data is ordered in a way that only the trailing n letters are meaningful. If you want to reduce the general length of your data and make it more compact.",

    },
    {
        "tool": "add-space-comma",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "simple",
        "h1": "Add Space after Comma",
        "h1description": "Adds a space after each Comma.",
        "metakeywords": "Online, Spreadsheet, Table, Add space after comma",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It adds a space after each comma. For example, the word 'Hey,you' will be turned into 'Hey, you' ",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains a lot of concatenated text that are comma separated. Adding space will make the data more readable for humans in general.",

    },
    {
        "tool": "join-text",
        "args": ["table"],
        "type": "text-mod",
        "complexity": "advanced",
        "h1": "Join Text Together",
        "h1description": "Combine each cell together to one cell.",
        "metakeywords": "Online, Spreadsheet, Table, Combine each row together, combine text",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "For each cell, the tool combines all text from the previous cells above together.",
        "_Q2": "When is it useful?",
        "_A2": "If you want aggregate text together cummulatively each cell by cell. Having a joined text gives information also about previous cells.",

    },

]

d_tools_math = [

    {
        "tool": "add-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Add Tables",
        "h1description": "Add two spreadsheets together.",
        "metakeywords": "Online, Spreadsheet, Table, Addition, Add, Combine, Plus",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It adds two tables together. For example, the first cell of the first table adds with the first cell of the second table. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data is separated in two or multiple tables and you want to add them together to calculate a final result.",

    },

    {
        "tool": "subtract-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Subtract Tables",
        "h1description": "Subtract 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Subtraction, Minus",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It subtracts the table B from table A. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data is separated in two or multiple tables and you want to subtract them together to calculate the difference between them.",

    },

    {
        "tool": "multiply-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Multiply Tables",
        "h1description": "Multiply 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Multiplication, Times",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It multiplies two tables together. For example, the first cell of the first table multiples with the first cell of the second table. ",
        "_Q2": "When is it useful?",
        "_A2": "If your data is separated in two or multiple tables and you want to multiply them together to calculate a final result.",

    },

    {
        "tool": "divide-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Divide Tables",
        "h1description": "Divide the data of 2 spreadsheets.",
        "metakeywords": "Online, Spreadsheet, Table, Division, Divide",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It divides table B from table A.",
        "_Q2": "When is it useful?",
        "_A2": "If your data is separated in two or multiple tables and you want to perform a division on them to calculate a final result.",

    },
    {
        "tool": "exponent-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Power Tables",
        "h1description": "Spreadsheet 1 acts as basis, spreadsheet 2 acts as exponent. ",
        "metakeywords": "Online, Spreadsheet, Table, Addition, Exponential, Base, Exponent",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It takes the first table as basis and takes the second table as exponent.",
        "_Q2": "When is it useful?",
        "_A2": "If your data is separated in two or multiple tables and you want to calculate the exponential result based on these two tables.",

    },

    {
        "tool": "abs-values",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Absolute Values",
        "h1description": "Turn negative values into positive values.",
        "metakeywords": "Online, Spreadsheet, Table, Absolute value, Negative to positive values",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It gives the absolute value of each numeric cell.",
        "_Q2": "When is it useful?",
        "_A2": "If you are only interested in the absolute number of your data and you want to convert them into positive numbers.",

    },

    {
        "tool": "round-values",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Round Values",
        "h1description": "Round each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Numbers",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It rounds each numeric values in a cell. If the cell contains text and numbers, the tool will also round the numbers.",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains numbers with too many decimals and you want to round to 2 decimals to improve readability.",

    },
    {
        "tool": "round-up",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Round Up",
        "h1description": "Round up each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Up, Ceiling Function",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It rounds up each numeric values in a cell. For example, 2.001 will be rounded to 3. If the cell contains text and numbers, the tool will also round the numbers.",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains numbers with too many decimals and you want to round upto improve readability.",

    },

    {
        "tool": "round-down",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Round Down",
        "h1description": "Round down each number of a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Round Down, Floor Function",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It rounds down each numeric values in a cell. For example, 2.99 will be rounded to 2. If the cell contains text and numbers, the tool will also round the numbers.",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains numbers with too many decimals and you want to round down decimals to improve readability.",

    },

    {
        "tool": "add-leading-zeros",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Add Leading Zeros",
        "h1description": "Add starting zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Add Start Zero, Begin Zeros",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It adds leading zeros in front of each text. For example, 8 will be turned into 08.",
        "_Q2": "When is it useful?",
        "_A2": "If you want all your data to have same length. If the number in your data means hours or room floors, you might want to have leading spaces in front of your data.",

    },

    {
        "tool": "add-trailing-zeros",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Add Trailing Zeros",
        "h1description": "Add ending zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Add Ending Zero, End zero",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It adds trailing zeros at the end of each text. For example, 8 will be turned into 80.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to add more digits to your numbers or if you want to fill numbers until they all have the same length.",

    },

    {
        "tool": "remove-leading-zeros",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Remove Leading Zeros",
        "h1description": "Remove starting zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Starting Zero, drop first zero",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It deletes leading zeros from any text. For example, 008 will be turned into 8.",
        "_Q2": "When is it useful?",
        "_A2": "If your data spreadsheet is copied from the internet, it sometimes contains unessesary leading zeros. Remove them will increase readability.",

    },

    {
        "tool": "remove-trailing-zeros",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Remove Trailing Zeros",
        "h1description": "Remove ending zeros to numbers in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Remove Ending Zero, drop last zero",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It deletes trailing zeros from any text. For example, 800 will be turned into 8.",
        "_Q2": "When is it useful?",
        "_A2": "If your data spreadsheet is copied from the internet, it sometimes contains unessesary ending zeros. Remove them will increase readability.",

    },

    {
        "tool": "sum",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Sum of Columns",
        "h1description": "Calculate the sum of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Summation of column",
        "colsize": "col-lg-8",

        "_Q1": "What does this tool do?",
        "_A1": "It calculates the sum of each column or row. This tool only calculates the sum of all numbers and ignores non number cells.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to quickly calculate the sum by row or column without doing it manually.",

    },

    {
        "tool": "average",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Average of Columns",
        "h1description": "Calculate the average of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Average of column",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It calculates the average value of each column or row. This tool only calculates the average of all numbers and ignores non number cells.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to quickly calculate the average by row or column without doing it manually.",

    },

    {
        "tool": "min",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Minimum of Columns",
        "h1description": "Calculate the minimum number of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Minimum of column",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It calculates the minimum of each column or row. This tool only calculates the minimum of all numbers and ignores non number cells.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to quickly calculate the minimum by row or column without doing it manually.",

    },

    {
        "tool": "max",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Maximum of Columns",
        "h1description": "Calculate the maximum number of each column in a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Maximum of column",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It calculates the maximum of each column or row. This tool only calculates the maximum of all numbers and ignores non number cells.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to quickly calculate the maximum by row or column without doing it manually.",

    },

    {
        "tool": "rank-table",
        "args": ["table"],
        "type": "math",
        "complexity": "advanced",
        "h1": "Rank Table",
        "h1description": "Rank each number of a spreadsheet in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Rank",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It creates a ranking for each cell based on the x-axis(column) or y-axis(row). The rank can be displayed in absolute number or in percentage.",
        "_Q2": "When is it useful?",
        "_A2": "Ranking is a statistical function. If you mainly want to know the value relative to other values.",

    },

    {
        "tool": "percentile-table",
        "args": ["table"],
        "type": "math",
        "complexity": "advanced",
        "h1": "Percentile Table",
        "h1description": "Pertent Rank each number of a spreadsheet in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Rank Percent",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It creates a ranking for each cell based on the x-axis(column) or y-axis(row). The rank can be displayed in percentage or in absolute number.",
        "_Q2": "When is it useful?",
        "_A2": "Percent Ranking is a statistical function. If you mainly want to know the value relative to other values.",

    },

    {
        "tool": "random-table",
        "args": ["table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Fill Random Number",
        "h1description": "Create a spreadsheet filled with random numbers.",
        "metakeywords": "Online, Spreadsheet, Table, Fill Numbers, Random Numbers",
        "colsize": "col-lg-6",
        "_Q1": "What does this tool do?",
        "_A1": "It generates a new table of your desired size and fill it with random numbers.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to test your formulas with random numbers, or if you want to have a placeholder for your future data.",

    },
]

d_tools_database = [

    {
        "tool": "transpose-table",
        "args": ["table"],
        "type": "database",
        "complexity": "simple",
        "h1": "Transpose Table",
        "h1description": "Swap spreadsheet column and row axis.",
        "metakeywords": "Online, Spreadsheet, Table, Transpose, Change Axis, Swap Orientation",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It swaps the column and row of a table. All data within the table are swaped accordingly.",
        "_Q2": "When is it useful?",
        "_A2": "If your data has a lot of columns and reading the data requires horizontal scrolling, you can swap the table axis to read it horizontally.",

    },

    {
        "tool": "sort-rows",
        "args": ["table"],
        "type": "database",
        "complexity": "simple",
        "h1": "Sort Tables",
        "h1description": "Sort spreadsheet rows in ascending or descending order.",
        "metakeywords": "Online, Spreadsheet, Table, Sort Rows, Sort Tables",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It sortes the table in ascending or descending order.",
        "_Q2": "When is it useful?",
        "_A2": "Sorting is a common spreadsheet function. It creates more meaning in the data by showing the biggest or smallest dataset first.",

    },

    {
        "tool": "unique-values",
        "args": ["table"],
        "type": "database",
        "complexity": "simple",
        "h1": "Unique Values",
        "h1description": "A Filter that only shows unique values of each columns.",
        "metakeywords": "Online, Spreadsheet, Table, Unique, Distinct, No Duplicate",
        "colsize": "col-lg-5",
        "_Q1": "What does this tool do?",
        "_A1": "It deletes all duplicates row.",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains duplicated, you can use this tool to clean up your spreadsheet. Having duplicated data will cause future analysis on the dataset to be wrong.",

    },

    {
        "tool": "drop-duplicated-columns",
        "args": ["table"],
        "type": "database",
        "complexity": "simple",
        "h1": "Drop Duplicated Columns",
        "h1description": "Remove columns with the same name.",
        "metakeywords": "Online, Spreadsheet, Table, Drop Duplicates, Remove Duplicates",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It deletes all duplicates row.",
        "_Q2": "When is it useful?",
        "_A2": "If your data contains duplicated, you can use this tool to clean up your spreadsheet. Having duplicated data will cause future analysis on the dataset to be wrong.",

    },

    {
        "tool": "join-tables",
        "args": ["table", "table"],
        "type": "database",
        "complexity": "advanced",
        "h1": "Join Tables",
        "h1description": "Merge two spreadsheets based on their key columns.",
        "metakeywords": "Online, Spreadsheet, Table, Join, Merge, Concat",
        "_Q1": "What does this tool do?",
        "_A1": "It takes two spreadsheets and merges them togehter based on their key columns.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to consolidate your data together. This tool is similar to the commonly used Vlookup function.",
        "_Q3": "What is the difference between Left Join, Right Join, Inner Join and Outer Join?",
        "_A3": """<ul>
          <li><b>Inner Join</b>: Returns records that have matching values in <b>both tables</b></li>
          <li><b>Left (Outer) Join</b>: Returns all records from the <b>left table</b>, and the matched records from the right table</li>
          <li><b>Right (Outer) Join</b>: Returns all records from the <b>right table</b>, and the matched records from the left table</li>
          <li><b>Full (Outer) Join</b>: Returns all records when there is a match in <b>either left or right table</b></li>
        </ul>""",
        "_Q4": "I uploaded both sheets, but it doesn't produce results.",
        "_A4": "A: Make sure the key of each sheet is in the first column and that they are named <b>exactly the same</b>. You can edit the column name in the online table directly.",

        "input.title": "Input Right Table",
        "input.descr": "Paste in your right table here.",
        "input2.title": "Input Left Table",
        "input2.descr": "Paste in your left table here.",
        "colsize": "col-lg-6",

    },

    {
        "tool": "group-by",
        "args": ["table"],
        "type": "database",
        "complexity": "advanced",
        "h1": "Group By Column",
        "h1description": "Group the entire spreadsheet by a desired column.",
        "metakeywords": "Online, Spreadsheet, Table, Group By, Grouping",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It performs a group and aggregation operation on the given spreadsheet. Possible aggregation functions are: sum, min, max, avg.",
        "_Q2": "When is it useful?",
        "_A2": "If your data has multiple entries and you want to summarize the data together for all entries.",

    },

]

d_tools_converter = [

    {
        "tool": "to-dsv",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to DSV",
        "h1description": "Save Spreadsheet as Delimiter Separated Values (dsv).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to DSV, Delimiter",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to .dsv (delimiter separated values) format.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to store the data in a more efficient format or if your other program requires a .dsv format input.",

    },

    {
        "tool": "to-csv",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to CSV",
        "h1description": "Save Spreadsheet as Comma Separated Values (csv).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to CSV, Comma",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to .csv (comma separated values) format.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to store the data in a more efficient format or if your other program requires a .csv format input.",

    },

    {
        "tool": "to-json",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to JSON",
        "h1description": "Save Spreadsheet as JavaScript Object Notation (json).",
        "metakeywords": "Online, Spreadsheet, Table, Convert to JSON, javascript object",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to .json (JavaScript Object) format.",
        "_Q2": "When is it useful?",
        "_A2": "If you are a programmer and need a table in json format. Json format are commonly used in http requests and network transfers.",

    },

    {
        "tool": "to-dict",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to Dictionary",
        "h1description": "Save Spreadsheet as Dictionary.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to Dictionary, Dict",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to dictionary format.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to store the data in a more efficient format or if your other program requires a dictionary as input.",

    },

    {
        "tool": "to-array",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to Array",
        "h1description": "Save Spreadsheet as Array.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to array",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to array format.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to store the data in a more efficient format or if your other program requires an array as input.",

    },

    {
        "tool": "to-collection",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "Table to Collection",
        "h1description": "Save Spreadsheet as collection.",
        "metakeywords": "Online, Spreadsheet, Table, Convert to collection",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It converts a spreadsheet to collection format.",
        "_Q2": "When is it useful?",
        "_A2": "If you want to store the data in a more efficient format or if your other program requires a collection as input.",

    },

    {
        "tool": "from-csv",
        "args": ["table"],
        "type": "converter",
        "complexity": "simple",
        "h1": "CSV to Table",
        "h1description": "Paste in CSV files to create a spreadsheet.",
        "metakeywords": "Online, Spreadsheet, Table, Convert from CSV, Comma",
        "colsize": "col-lg-8",
        "_Q1": "What does this tool do?",
        "_A1": "It takes a csv and converts it to online editable spreadsheet.",
        "_Q2": "When is it useful?",
        "_A2": "If you have no tool to open a csv locally on your computer, you can use this tool to edit the table directly online.",

    },

]

# s for specific. specific tool dict
d_tools_txt_s = d_tools_filter + d_tools_text + d_tools_math + d_tools_database + d_tools_converter

# same for all faq tools
d_tools_faq_g = {
    "_Q100": "Can I upload my data as .xlsx or .csv file?",
    "_A100": "Upload data as .xlsx or .csv file is not supported yet. You can copy paste your data from excel into the website table above.",
    "_Q101": "Is there a limit to the size of the spreadsheet I can upload?",
    "_A101": "Yes it can handle tables up to 6000 columns and rows. If you encounter lag, you can reduce the sheet size.",
    "_Q102": "It is normal that it lags a couple of seconds during copy paste?",
    "_A102": "Yes this is normal for a web based application (especially when the data set is large).",
    "_Q103": "The provided spreadsheet interface is very small. Can you make it bigger?",
    "_A103": "It is recommended to paste data into Excel to manage a bigger data sets.",
    "_Q104": "What plugin do you use to build this tool?",
    "_A104": "Bootstrap, Handsontable.js and dataframe.js.",
    "_Q105": "Is the sicksheet.com free to use?",
    "_A105": "There is no charge for uploading your spreadsheet and using any online tool. However, donations to support the SickSheet project are appreciated.",
    "_Q106": "Who can I contact if I have a problem or question about the First N Rows tool?",
    "_A106": "You can write a public post <a href='https://www.reddit.com/r/sicksheet/comments/11looge/official_bug_list/'>here.</a>",
    "_Q107": "Is my data secure when I use the First N Rows tool?",
    "_A107": "Yes, the tool is pure client side which means we don't receive any data from you.",
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
        function.nav: [[{"nav_text": "Blog", "nav_url": "blog/index.html"}, ], []]
    },
    {
        "blog_url": "shoulderofgiants.com",
        "blog_logo": "Shoulder of Giants",
        "title": "ShoulderofGiants",
        "lang": "en",
        "metadescription": "A collection of spreadsheet tools online. Each tool is specifically design to solve one spreadsheet problem.",
        "metakeywords": "Online, Spreadsheet, Table, Micro Saas",
        "redirect": "blog/index.html",
        function.nav: [[{"nav_text": "Blog", "nav_url": "blog/index.html"}, ], []]
    },
    {
        "blog_url": "sicksheet.com",
        "blog_logo": "SICK.SHEET",
        "title": "SickSheet",
        "lang": "en",
        "metadescription": "This blog is a collection of useful career tips to help you climb up the career ladder.",
        "metakeywords": "career, tips, corporate ladder",
        "redirect": "tools/index.html",
        function.nav: [[{"nav_text": "Tools", "nav_url": "tools/index.html"},
                        ],
                       # {"nav_text": "Blog", "nav_url": "blog/index.html"}, ],
                       [{"nav_text": "Filter", "nav_url": "index.html#filter"},
                        {"nav_text": "Text", "nav_url": "index.html#text-mod"},
                        {"nav_text": "Math", "nav_url": "index.html#math"},
                        {"nav_text": "Database", "nav_url": "index.html#database"},
                        {"nav_text": "Converter", "nav_url": "index.html#converter"},
                        ]]
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


 {
        "tool": "dot-product-tables",
        "args": ["table", "table"],
        "type": "math",
        "complexity": "simple",
        "h1": "Dot Product Tables",
        "h1description": "Scalar product the data of 2 tables into a new table.",
        "metakeywords": "Online, Spreadsheet, Table, Scalar Product, Dot Product, Matrix Product",
        "input.title": "Input First Table",
        "input.descr": "Paste in your first table here.",
        "input2.title": "Input Second Table",
        "input2.descr": "Paste in your second table here.",
    },
"""
