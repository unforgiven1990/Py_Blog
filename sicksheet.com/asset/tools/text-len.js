

function tool() {
    data=hot1.getData()
    result=[]

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }
console.log("as")
    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
            mystring=String(data[i][j])
            result[i][j] = mystring.length
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