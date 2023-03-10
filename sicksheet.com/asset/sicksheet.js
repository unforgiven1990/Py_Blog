
color1 = "#d3eaf2"
color2 = "#f8d7da"//alert danger
color3 = "#fff3cd"//alert warning
color4 = "#d4edda"//alert success

function example1(){
return {
    "#table1": [
        ['Name', 'Age', 'Car Brand'],
        ['Ali', "20", "NIO"],
        ['Max', "33", "Tesla"],
        ['James', "27", "BMW"],
        ['Jane', "25", "Mercedes"],
    ],
    "#table2": [
        ['Name', 'Country', 'Height'],
        ['Ali', "Italy", "1.7"],
        ['Eric', "USA", "1.8"],
        ['Jane', "Germany", "1.6"],
        ['Anna', "Japan", "1.7"],
    ],
    "#table3": [],
}
}


//set color of table 1 and 2
function setColorRow(hot, color = "#fff", rowindex = 0) {
    var rows = hot.countRows(); // get the count of the rows in the table
    for (var row = 0; row < rows; row++) { // go through each row of the table
        var cell = hot.getCell(row, rowindex)
        try{
        cell.style.background = color
        }catch{}

    }
}

function setColorColumn(hot, color = "#fff", colindex = 0) {
    var cols = hot.countCols(); // get the count of the rows in the table
    for (var col = 0; col < cols; col++) { // go through each row of the table
        var cell = hot.getCell(colindex, col);
        try{
        cell.style.background = color
        }catch{}
    }
}
function isNumber(n) { return !isNaN(parseFloat(n)) && !isNaN(n - 0) }


function setColorNonNumeric(hot, color = color3) {
    var cols = hot.countCols(); // get the count of the rows in the table
    var rows = hot.countRows(); // get the count of the rows in the table
    has_non_numeric=false
    for (var col = 0; col < cols; col++) { // go through each row of the table
        for (var row = 0; row < rows; row++) {
            var cell = hot.getCell(row, col)
            if (!isNumber(hot.getDataAtCell(row,col))){
                cell.style.background = color
                has_non_numeric=true
            }
        }
    }
    return has_non_numeric
}


function setColorNumeric(hot, color = color4) {
    var cols = hot.countCols(); // get the count of the rows in the table
    var rows = hot.countRows(); // get the count of the rows in the table
    has_non_numeric=false
    for (var col = 0; col < cols; col++) { // go through each row of the table
        for (var row = 0; row < rows; row++) {
            var cell = hot.getCell(row, col)
            if (isNumber(hot.getDataAtCell(row,col))){
                cell.style.background = color
                has_non_numeric=true
            }
        }
    }
    return has_non_numeric
}

function myexport2(){
//download txt file instead of csv file
data=encodeURIComponent($('#mycode').html())
window.open('data:text/plain;charset=utf-8,' + data)
}

function myexport(hot, name) {
    //setup download button
    const exportPlugin = hot.getPlugin('exportFile')
    const button = document.querySelector('#download')
    button.addEventListener('click', () => {
        $('#exampleModal').modal("show")
        exportPlugin.downloadFile('csv', {
            bom: false,
            columnDelimiter: ',',
            columnHeaders: false,
            exportHiddenColumns: true,
            exportHiddenRows: true,
            fileExtension: 'csv',
            filename: name.replace("-"," ") + ' [YYYY].[MM].[DD]',
            mimeType: 'text/csv;charset=utf-8,',
            rowDelimiter: '\r\n',
            rowHeaders: true
        })
    })


}


function datainit(mydata) {
    return {
        data: mydata,
        rowHeaders: true,
        colHeaders: true,
        contextMenu: true,
        readOnly: false,
        renderAllRows: false,
        manualRowMove: true,
        manualColumnMove: true,
        colWidths: 100,
        width: '100%',
        height: 150,
        viewportColumnRenderingOffset: 5,
        viewportRowRenderingOffset: 5,

        licenseKey: 'non-commercial-and-evaluation'
    }
}


function downloadCSV() {
    //doenst work yet
    var str = encodeURIComponent($('div[id$=table3] > .ht_master').html())
    var uri = 'data:text/csv;charset=utf-8,' + str;

    var downloadLink = document.createElement("a");
    downloadLink.href = uri;
    downloadLink.download = "joined.csv";

    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

function downloadEXCEL() {
    window.open('data:application/vnd.ms-excel' + encodeURIComponent($('div[id$=table3] > .ht_master').html()));
}


function download_text(filename="data.csv",button_id="#download", content="#mycode"){
    // Start file download.
       $(button_id).click(function(){
           content=$(content).html()
           download(filename, content)
       })
}

//download that works
function download(filename, text) {
       var element = document.createElement('a');
       element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
       element.setAttribute('download', filename);
       element.style.display = 'none';
       document.body.appendChild(element);
       element.click()
       document.body.removeChild(element)
}



function listener_configure(a_elements,a_functions=[],event="change"){
    a_functions.push(tool)
    $.each(a_elements, function(arrakey, element) {
        $.each(a_functions, function(funckey, func) {
            $(element).bind(event,function(){
              func()
            })
        })
    })
}

function listener_table(a_elements,a_functions=[]){
    a_functions.push(tool)
    a_hooks=[
    "afterChange",
    "afterCreateCol",
    "afterCreateRow",
    "afterRemoveCol",
    "afterRemoveRow",
    "afterColumnSort",
    //"afterRowSort",
    "afterColumnMove",
    "afterRowMove",
    "afterColumnExpand",
    "afterRowExpand",
    "afterAutofill",
    ]
    $.each(a_elements, function(arrakey, hot) {
        $.each(a_functions, function(funckey, func) {
            $.each(a_hooks, function(hookkey, hookfunc) {
                hot.addHook(hookfunc, (row, amount) => {
                  func()
                })
            })
        })
    })
}

function hot_to_dataframe(hot,col=true){
    //dataiscol =first column data is column
    //
    if (col){
    hot_data = hot.getData()
    hot_column = hot_data[0]
    hot_data.shift()
    return new dfjs.DataFrame(hot_data, hot_column)
    }else{
    hot_data = hot.getData()
    console.log("3 hot_data ",hot_data)
    return new dfjs.DataFrame(hot_data)
    }
}

function hot_to_danfo(hot){
    hot_data = hot.getData()
    hot_column = hot_data[0]
    return new dfd.DataFrame(hot_data,{columns:hot_column})
}


function data_to_hot(id,datawithcol){
    $(id).handsontable(datainit(datawithcol))
    hot = $(id).handsontable('getInstance')
    hot.updateSettings({
        //readOnly: true, // make table cells read-only
        editor: false
    })
}




function main() {
    /*
    Meta logic. If nothing specified in each tool, use the default one. Else: replace.
    create_input()// always the same table
    create_configure ()// different each
    initiate_options()//setup and fill values for options
    create_output()//always the download table
    tool()//the main tool function itself
    input_onchange() // event trigger. binds to list of elements
    configure_onchange() // event trigger
    init()// to start the tool, eg. hiding something
    */
    try{
        d_data = exampletool()
    }catch{
        d_data = example1()
    }

    for (let [index, item] of ["#table1", "#table2", "#table3"].entries()) {
        try {
            $(item).handsontable(datainit(data = d_data[item]))
        } catch {
        //todo for the third table id
        }
    }

    $(".mytooltip").tooltip()
    //$(".accordion-item .accordion-collapse").first().addClass("show")
    /**
    $('#download').on('click', function() {
        $('#exampleModal').show()
    })**/
    hot1 = $("#table1").handsontable('getInstance')
    hot2 = $("#table2").handsontable('getInstance')
    hot3 = $("#table3").handsontable('getInstance')
    try{//because not every tool has a download button
        myexport(hot2, $("header").data("tool"))
    }catch{
    }

    init()

    //pyodided_test()
}
function isNumber(n) { return !isNaN(parseFloat(n)) && !isNaN(n - 0) }

//init
$(document).ready(main)


function addTwoNumbers(x, y){
        return x + y;
    }


async function pyodided_test(){
namelol = "Jeff"
let pyodide = await loadPyodide()
 //await pyodide.loadPackage("pandas")
console.log(pyodide.runPython(`
    #import pandas as pd
    import js

    from js import namelol, addTwoNumbers, console
    js.myname=namelol+"fuu yeah house"
    print("Hello " + namelol + ".Adding 1 and 2 in Javascript: " + str(addTwoNumbers(1, 2)))


`));

console.log(myname)
}


