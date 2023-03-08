function tool() {
    df = hot_to_dataframe(hot1).sample($('#n').val()*0.01)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}


function config(){
$('#n').attr('min', 0)
$('#n').attr('max', 100)
$('#n_label').html("Sample "+$('#n').val()+"%:")
}


//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[config])
    listener_configure(["#sample"],[config],"click")

    $('#n').attr('value',37)
    config()
    tool()
}