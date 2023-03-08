

function tool() {
    data=hot1.getData()
    result=[]
    left=$("#n").val()

    countRows = hot1.countRows()
    countCols = hot1.countCols()

    for (var i = 0; i < countRows; i++) {
      result[i] = new Array(countCols);
    }

    for (var i = 0; i < countRows; i++) {
        for (var j = 0; j < countCols; j++) {
            result[i][j] = String(data[i][j]).substring(0,left)
        }
    }
    datawithcol = result
    data_to_hot("#table2",datawithcol)
}


function config(){
data=hot1.getData()
countRows = hot1.countRows()
countCols = hot1.countCols()
maxnumber=0
for (var i = 0; i < countRows; i++) {
    for (var j = 0; j < countCols; j++) {
        potential=String(data[i][j]).length
        if (potential > maxnumber){
            maxnumber=potential
        }
    }
}

$('#n').attr('min', 1)
$('#n').attr('max', maxnumber)
displaylabel()
}

function displaylabel(){
$('#n_label').html("Left "+$('#n').val()+" Characters")
}

//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[displaylabel])

    $('#n').attr('value',3)
    config()
    tool()
}