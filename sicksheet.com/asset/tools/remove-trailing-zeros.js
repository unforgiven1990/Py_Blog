function exampletool(){
return  {
"#table1": [

         ["10000", "000200", "0300000"],
         ["2200", "03300000", "006"],
         ["722000000", "822022", "2222000"],
         ["1023000", "112300", "12110"],
    ]
}
}

function removeLeadingZeros(str, n) {
  const regex = new RegExp(`^0{0,${n}}`); // create a RegExp to match the first n leading zeros
  console.log(regex)
  const removedZeros = str.replace(regex, ''); // remove the matched zeros from the string
  return removedZeros;
}

function removeTrailingZeros(str, n = 0) {
  const regex = new RegExp(`0{0,${n}}$`); // create a RegExp to match the last n trailing zeros
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
                result[i][j] = removeTrailingZeros(data[i][j],decimals)
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