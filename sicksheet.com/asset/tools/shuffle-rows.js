function tool() {
console.log("shuffle")
    df = hot_to_dataframe(hot1).shuffle()
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}

//init function
function init() {
    listener_table([hot1])
    listener_configure(["#shuffle"],[],"click")
    tool()
}