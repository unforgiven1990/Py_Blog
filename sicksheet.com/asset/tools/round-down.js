function exampletool(){
return  {
"#table1": [

         ["Number A is 2.33", "Number B is 79.3", "Number C is 11.357"],
         [4.2, 5.2, 6.0],
         [7.22, 8.1, 9.2345],
         [10.233, 11.23, 12.1],
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
        //if the data is stirng+ number
            myvar=data[i][j]
            if (typeof myvar === 'string'){
                finalstring=""
                $.each(myvar.split(" "), function(key, value) {
                    if (isNumber(value)){
                        console.log(value)
                        finalstring=finalstring+" "+String(Math.floor(parseFloat(value)))
                    }else{
                        finalstring=finalstring+" "+value
                    }

                })
                result[i][j] = finalstring
            }else if (isNumber(myvar)){
                result[i][j] = Math.floor(myvar)
            }
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