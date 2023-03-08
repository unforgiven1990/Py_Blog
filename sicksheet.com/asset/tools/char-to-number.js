function exampletool(){
return  {
"#table1": [
         ["a", "b", "c"],
         ["d", "e", "f"],
         ["g", "h", "i"],
         ["j", "k", "l"],
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
            result[i][j] = charToNum(data[i][j])
        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}

function charToNum(char) {
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  index = alphabet.indexOf(char)
  return index + 1;
}

//init function
function init() {
    listener_table([hot1])
    tool()
}