function tool() {
    df = hot_to_dataframe(hot1).transpose()
    datawithcol = [].concat(df.toArray())
    data_to_hot("#table2",datawithcol)

    //add little highlight to indicate the swapped result
    setColorColumn(hot1, color1)
    setColorRow(hot2, color1)
}


//init function
function init() {
    listener_table([hot1])
    tool()
}