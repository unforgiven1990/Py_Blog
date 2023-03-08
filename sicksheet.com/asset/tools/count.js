function tool() {
    df=hot_to_dataframe(hot1,col=true)
    result=[[],[]]
    $.each(df.listColumns(), function(counter, val) {
         result[0][counter]=val

         console.log(df[val])
         result[1][counter]=df.stat.count(val)
    })

    datawithcol = result
    data_to_hot("#table2",datawithcol)
    setColorNumeric(hot1)
}

function init() {
    listener_table([hot1])
    tool()
}


