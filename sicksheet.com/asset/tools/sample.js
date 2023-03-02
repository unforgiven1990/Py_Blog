function initiate_options() {
    $('#n').attr('max', data1 = 100)
    $('#n').change(function() {
        tool()
    })

    $('#sample').click(function() {
        tool()
    })
}


function tool() {
    //get data
    data1 = hot1.getData()
    colheader1 = data1[0]
    data1.shift()
    n=$('#n').val()
    n=n*0.01

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = df1.sample(n)
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

    //called everytime input refreshes
    initiate_options()

    //called only first time
}