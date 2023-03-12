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
    setColor(hot=hot1,  bgclass = "bg-green" , rowindex=0, colindex=-1)
    setColor(hot=hot2,  bgclass = "bg-green" , rowindex=-1, colindex=0)
}


//init function
function init() {
    listener_table([hot1])
    tool()
}