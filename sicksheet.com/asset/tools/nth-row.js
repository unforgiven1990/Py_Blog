

function tool() {
    data=hot1.getData()
    n=$("#n").val()
    datawithcol = result = data.filter((a,i) => i%n===0);
    console.log(result)
    data_to_hot("#table2",datawithcol)
}


function config(){
data=hot1.getData()
countRows = hot1.countRows()-1

$('#n').attr('min', 1)
$('#n').attr('max', countRows)
displaylabel()
}

function displaylabel(){
$('#n_label').html("Get every "+$('#n').val()+"th Row")
}

//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[displaylabel])

    $('#n').attr('value',2)
    config()
    tool()
}