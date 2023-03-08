function tool() {
    df=hot_to_dataframe(hot1,col=true)
    result=[[],[]]
    $.each(df.listColumns(), function(counter, val) {
         result[0][counter]=val
         result[1][counter]=df.stat.mean(val)
    })

    datawithcol = result
    data_to_hot("#table2",datawithcol)
    setColorNumeric(hot1)
}

function init() {
    listener_table([hot1])
    tool()
}


