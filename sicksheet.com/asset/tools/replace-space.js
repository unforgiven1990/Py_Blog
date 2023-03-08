function exampletool(){
return  {
"#table1": [
        ['Name', 'Age', 'Car Brand'],
        ['Ali Baba', "20", "Mercedes Benz"],
        ['Max Muster', "33", "Tesla"],
        ['Dr. Dre', "27", "BMW"],
        ['Emi lia', "25", "Mercedes Benz"],
    ]
}
}

function tool() {

    data=hot1.getData()
    result=[]
    replace_sign=$("#replace").val()

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }

    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
            try{
                result[i][j] = data[i][j].replace(" ",replace_sign)
            }catch{
                result[i][j] = data[i][j]
            }

        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}

function config(){
    data1 = hot1.getData()
    columns = data1[0]
    $('#replace').html("")
    $('#replace').append('<option value="_">Underscore _</option>')
    $('#replace').append('<option value=".">Dot .</option>')
    $('#replace').append('<option value="·">Interpunct ·</option>')
    $('#replace').append('<option value="-">Minus Sign -</option>')
    $('#replace').append('<option value="+">Plus Sign +</option>')
    $('#replace').append('<option value=",">Comma ,</option>')
    $('#replace').append('<option value=";">Semicolon ;</option>')
    $('#replace').append('<option value="\n">New Line </option>')
}

//init function
function init() {
    listener_table([hot1])
    listener_configure(["#replace"])
    config()
    tool()
}