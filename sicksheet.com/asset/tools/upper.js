function exampletool(){
return  {
"#table1": [
        ['Name', 'Age', 'Car Brand'],
        ['ali', "20", "nio"],
        ['max', "33", "tesla"],
        ['James', "27", "BMW"],
        ['jane', "25", "mercedes"],
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
                s=data[i][j]
                result[i][j] = s.toUpperCase()
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