function tool() {

    df = hot_to_dataframe(hot1).transpose(transposeColumnNames=true)

    //manually change column order
    columns=df.listColumns()
    data=df.toArray()
    $.each(data, function(key, array) {
        array.unshift(array.pop())
    })

    /** doesnt work because of to df.toArray() takes order instead of key
    columns=df.listColumns()
    columns.unshift(columns.pop())
    df=df.restructure(columns)
    console.log(columns)
    console.log(df)**/

    datawithcol = [].concat(data)
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