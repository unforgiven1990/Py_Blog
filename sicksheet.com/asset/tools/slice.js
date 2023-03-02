function tool() {
    //get data
    data1 = hot1.getData()
    colheader1 = data1[0]
    data1.shift()
    start=$('#startn').val()
    end=$('#endn').val()
    console.log(start)
    console.log(end)
    console.log("--")

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = df1.slice(start,end)
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
    listener_configure(["#startn","#endn"])

    max=hot1.countRows()-1
    $('#endn').attr('max', max)
    $('#startn').attr('max', max)
    $('#startn').attr('min', 0)
    $('#endn').attr('min', 0)
    $('#startn').value(0)
    $('#endn').value(Math.round(max*0.7))
    tool()
}