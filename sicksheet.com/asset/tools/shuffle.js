

function tool() {
console.log("tool shuffle")
    //get data
    data1 = hot1.getData()
    colheader1 = data1[0]
    data1.shift()

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = df1.shuffle()
    datawithcol = [df2.listColumns()].concat(df2.toArray())

    //create table
    $("#table2").handsontable(datainit(data = datawithcol))
    hot2 = $("#table2").handsontable('getInstance')
    hot2.updateSettings({
        //readOnly: true, // make table cells read-only
        editor: false
    });
}


//init function
function init() {
    listener_table([hot1])
    listener_configure(["#shuffle"])
    tool()
}