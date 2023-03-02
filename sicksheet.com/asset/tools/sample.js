function tool() {
    df = hot_to_dataframe(hot1).sample($('#n').val()*0.01)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}


//init function
function init() {
    listener_table([hot1])
    listener_configure(["#sample","#n"])
     $('#n').attr('max', data1 = 100)
    tool()
}