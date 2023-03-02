function tool() {
    start=$('#startn').val()
    end=$('#endn').val()
    df = hot_to_dataframe(hot1).slice(start,end)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)

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