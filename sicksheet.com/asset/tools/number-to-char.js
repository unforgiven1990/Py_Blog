function exampletool(){
return  {
"#table1": [
         [1, 2, 3],
         [4, 5, 26],
         [727, 8, 9],
         [10, 111, 128],
         [132, 14, 15],
    ]
}
}

function convert(num) {
    return num
        .toString()    // convert number to string
        .split('')     // convert string to array of characters
        .map(Number)   // parse characters as numbers
        .map(n => (n || 10) + 64)   // convert to char code, correcting for J
        .map(c => String.fromCharCode(c))   // convert char codes to strings
        .join('');     // join values together
}


function convertintChar(integer) {
 let character = 'a'.charCodeAt(0)
 return String.fromCharCode(character + integer-1)
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
            result[i][j] = convertintChar(parseInt(data[i][j]))
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