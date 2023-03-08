function exampletool(){
return  {
"#table1": [
        ['Name', 'Age', 'Car Brand'],
        ['ali baba', "20", "nio"],
        ['max muster', "33", "tesla"],
        ['james bond', "27", "BMW"],
        ['jane blue', "25", "mercedes benz"],
    ]
}
}

function toTitleCase(str) {
  return str.replace(
    /\w\S*/g,
    function(txt) {
    if (txt==txt.toUpperCase(txt)){
            return txt
        }else{
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
        }
    }
  );
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
                result[i][j] = toTitleCase(data[i][j])
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