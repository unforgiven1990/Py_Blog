function tool() {
    df=hot_to_dataframe(hot1,col=true)
    result=[[],[]]
    $.each(df.listColumns(), function(counter, val) {
         result[0][counter]=val
         try{
            result[1][counter]=df.stat.max(val)
         }catch{
            result[1][counter]=0
         }
    })

    datawithcol = result
    data_to_hot("#table2",datawithcol)
    setColorNumeric(hot1)
}

function init() {
    listener_table([hot1])
    tool()
}


