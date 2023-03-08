function createNdArray(col, row, d) {
   result=[]
  for (k = 0; k < row; k++) {
    result[k]=Array.from({length: col}, () => Math.floor(Math.random() * Math.pow(10,d)) );
  }
  return result
}


function tool() {
    col = $("#col").val()
    row = $("#row").val()
    digits = $("#digits").val()

    datawithcol =createNdArray(col,row,digits)
    data_to_hot("#table2",datawithcol)
}

function update_display(){
$('#row').attr('min', 1)
$('#row').attr('max', 30)

$('#row_label').html(""+$('#row').val()+" Rows")

$('#col').attr('min', 1)
$('#col').attr('max', 30)

$('#col_label').html(""+$('#col').val()+" Columns")

$('#digits').attr('min', 1)
$('#digits').attr('max', 10)

$('#digits_label').html(""+$('#digits').val()+" Digits")
}

function init() {
    listener_configure(["#row","#col","#digits"],[update_display])

    $('#col').attr('value', 3)
    $('#row').attr('value', 5)
    $('#digits').attr('value', 3)
    update_display()
    tool()
}