function exampletool(){
return  {
"#table1": [

         [1.2345, 2.2345, 3.223],
         [4.2, 5.2, 6.0],
         [7.22, 8.1, 9.2345],
         [10.233, 11.23, 12.1],
    ],

"#table2": [
        [1, 2, 4],
        [2, 2, 3],
        [3, 2, 3],
        [4, 2, 3],
    ],
}
}

function tool() {
console.log("called")
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
            result[i][j] = data[i][j].toFixed(decimals)
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