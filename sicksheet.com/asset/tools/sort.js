function initiate_options() {
    data1 = hot1.getData()
    columns = data1[0]
    $('#sortcol').html("")
    $.each(columns, function(index, val) {
        $('#sortcol').append('<option value="' + val + '">Sort by ' + val + '</option>')
    })

    $('#asc').html("")
    $('#asc').append('<option value="true">In Ascending Order</option>')
    $('#asc').append('<option value="false">In Descending Order</option>')

}


function tool() {
    //get data
    data1 = hot1.getData()
    sortcol = $("#sortcol option:selected").val()
    asc = $("#asc option:selected").val()
    asc = (asc === 'true');
    colheader1 = data1[0]
    data1.shift()

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = df1.sortBy(sortcol, asc)
    datawithcol = [df2.listColumns()].concat(df2.toArray())


    //create table
    $("#table2").handsontable(datainit(data = datawithcol))
    hot2 = $("#table2").handsontable('getInstance')
    hot2.updateSettings({
        //readOnly: true, // make table cells read-only
        editor: false
    });

    //add little highlight to indicate the swapped result
    colindex = colheader1.indexOf(sortcol)
    setColorRow(hot2, color1, colindex)
}



function init() {
    //init function

    hot1.addHook('afterChange', (row, amount) => {
        initiate_options()
        tool()
    })

    $('#sortcol').change(function() {
        tool()
    })
    $('#asc').change(function() {
        tool()
    })

    initiate_options()

    $("#sortcol").val("Age")
    $("#sortcol").trigger("change")
    //$("#sortcol").val("Age")
    //$("#sortcol").trigger("change")

}