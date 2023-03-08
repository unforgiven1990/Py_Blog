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
function config(){
    data1 = hot1.getData()
    columns = data1[0]
    $('#sortcol').html("")
    $.each(columns, function(index, val) {
        $('#sortcol').append('<option value="' + val + '">' + val + '</option>')
    })
}


function init() {
    listener_table([hot1],[config])
    listener_configure(["#sortcol","#asc"])
    config()

    //one time call
    $('#asc').html("")
    $('#asc').append('<option value="true">Ascending</option>')
    $('#asc').append('<option value="false">Descending</option>')
    var lastValue = $('#sortcol option:last-child').val()
    $("#sortcol").val(lastValue)
    $("#sortcol").trigger("change")
    tool()
}