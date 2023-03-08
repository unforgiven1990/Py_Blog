function tool() {
    uniquecol = $("#unique option:selected").val()
    df = hot_to_dataframe(hot1).unique(uniquecol)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)

    //add little highlight to indicate the swapped result
    colindex = colheader1.indexOf(sortcol)
    setColorRow(hot2, color1, colindex)
}
function config(){
    data1 = hot1.getData()
    columns = data1[0]
    $('#unique').html("")
    $.each(columns, function(index, val) {
        $('#unique').append('<option value="' + val + '">' + val + '</option>')
    })
}


function init() {
    listener_table([hot1],[config])
    listener_configure(["#unique"])
    config()

    //one time call
    var lastValue = $('#unique option:last-child').val()
    $("#unique").val(lastValue)
    $("#unique").trigger("change")
    tool()
}