function tool() {
    df = hot_to_dataframe(hot1).head($('#n').val())
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}

function config(){
$('#n').attr('min', 0)
$('#n').attr('max', hot1.countRows()-1)
$('#n_label').html("Last "+$('#n').val()+" Row:")
}

//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#n"],[config])

    max=hot1.countRows()-1
    $('#n').attr('value', Math.round(max*0.3))
    config()
    tool()

}