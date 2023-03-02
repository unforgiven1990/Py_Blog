function tool() {
    sortcol = $("#sortcol option:selected").val()
    asc = $("#asc option:selected").val()
    asc = (asc === 'true')
    df = hot_to_dataframe(hot1).sortBy(sortcol, asc)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)

    //add little highlight to indicate the swapped result
    colindex = colheader1.indexOf(sortcol)
    setColorRow(hot2, color1, colindex)
}



function init() {
    //init function

    listener_table([hot1])
    listener_configure(["#sortcol","#asc"])


    data1 = hot1.getData()
    columns = data1[0]
    $('#sortcol').html("")
    $.each(columns, function(index, val) {
        $('#sortcol').append('<option value="' + val + '">Sort by ' + val + '</option>')
    })

    $('#asc').html("")
    $('#asc').append('<option value="true">In Ascending Order</option>')
    $('#asc').append('<option value="false">In Descending Order</option>')

    $("#sortcol").val("Age")
    $("#sortcol").trigger("change")
    //$("#sortcol").val("Age")
    //$("#sortcol").trigger("change")
    tool()
}