function exampletool(){
return  {
"#table1": [
         [1.0, -2.1, -3.2],
         [4.2, -5.2, -6.0],
         [7.22, -8.1, 9.2],
         [-10.0, 11, 4.0],
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
            result[i][j] =absnumber= Math.floor(number)
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