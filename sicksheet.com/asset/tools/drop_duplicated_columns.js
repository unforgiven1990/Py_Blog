function tool() {
    selected_col = $("#duplicate option:selected").val()
    df = hot_to_dataframe(hot1).dropDuplicates()
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}


//init function
function init() {
    listener_table([hot1])
    listener_configure(["#duplicate"])

    //put duplicates to select
    data1 = hot1.getData()
    columns = data1[0]
    $('#duplicate').html("")
    $.each(columns, function(index, val) {
        $('#duplicate').append('<option value="' + val + '">Drop Duplicates for Column:  ' + val + '</option>')
    })

    tool()
}

