function initiate_options() {
    $('#n').attr('max', data1 = hot1.countRows()-1)
}


function tool() {
    //get data
    data1 = hot1.getData()
    colheader1 = data1[0]
    data1.shift()
    n=$('#n').val()

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = df1.head(n)
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
    hot1.addHook('afterChange', (row, amount) => {
        initiate_options()
        tool()
    })

    $('#n').change(function() {
        tool()
    })

    initiate_options()
}