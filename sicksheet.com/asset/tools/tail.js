function tool() {
    n=$('#n').val()
    df = hot_to_dataframe(hot1).tail(n)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}

//init function
function init() {
    listener_table([hot1])
    listener_configure(["#n"])
    $('#n').attr('max', data1 = hot1.countRows()-1)
    tool()
}