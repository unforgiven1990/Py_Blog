function exampletool(){
return  {
"#table1": [
        ['Name', 'Age', 'Car Brand'],
        ['  Ali ', "20", "NIO"],
        ['Max', "33 ", " Tesla"],
        [' James', " 27 ", " BMW"],
        [' Jane', "25", " Mercedes"],
    ]
}
}

function tool() {
    data=hot1.getData()
    result=[]
    decimals=$("#n").val()

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }

    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
            try{
                result[i][j] = data[i][j].trimStart()
            }catch{
                result[i][j] = data[i][j]
            }

        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}


function config(){
$('#n').attr('min', 0)
$('#n').attr('max', 6)
$('#n_label').html("Round "+$('#n').val()+" digits")
}


//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[config])

    $('#n').attr('value',1)
    config()
    tool()
}