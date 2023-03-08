function exampletool(){
return  {
"#table1": [

         ["00001", "0002", "0003"],
         ["0022", "0033", "006"],
         ["00722", "822022", "02222"],
         ["00001023", "001123", "1211"],
    ]
}
}

function removeLeadingZeros(str, n) {
  const regex = new RegExp(`^0{0,${n}}`); // create a RegExp to match the first n leading zeros
  console.log(regex)
  const removedZeros = str.replace(regex, ''); // remove the matched zeros from the string
  return removedZeros;
}

function tool() {
    data=hot1.getData()
    result=[]
    decimals=$("#n").val()
    decimals=parseInt(decimals)
    console.log(decimals)

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }

    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
            try{
                result[i][j] = removeLeadingZeros(data[i][j],decimals)
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
$('#n_label').html("Remove "+$('#n').val()+" leading zeros")
}


//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[config])

    $('#n').attr('value',8)
    config()
    tool()
}