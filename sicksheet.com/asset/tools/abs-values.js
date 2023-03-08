function exampletool(){
return  {
"#table1": [
         [-1, -2, -3],
         [-4.2, -5.2, -6],
         [7.22, -8.1, 9.2345],
         [-10.233, 11.23, "this is not a number"],
    ]
}
}

function tool() {
    data=hot1.getData()
    result=[]

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }

    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
        try{

            number=parseFloat(data[i][j])
            result[i][j] =absnumber= Math.abs(number)
            if (isNaN(parseFloat(absnumber))){
                result[i][j] = data[i][j]
            }
        }catch{
            result[i][j] = data[i][j]
        }
        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}


//init function
function init() {
    listener_table([hot1])
    tool()
}