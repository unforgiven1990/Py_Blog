function exampletool(){
return  {
"#table1": [

         [1, 2, 3],
         [22, 33, 66],
         [722, 822, 922],
         [1023, 1123, 1211],
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
            result[i][j] = String(data[i][j]).padEnd(decimals, '0')
        }
        catch{
            result[i][j] = data[i][j]
        }

        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}


function config(){
$('#n').attr('min', 0)
$('#n').attr('max', 12)
$('#n_label').html("Pad to "+$('#n').val()+" leading zeros")
}


//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[config])

    $('#n').attr('value',3)
    config()
    tool()
}