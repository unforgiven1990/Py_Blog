function tool() {
    start=$('#startn').val()
    end=$('#endn').val()
    df = hot_to_dataframe(hot1).slice(start,end)
    datawithcol = [df.listColumns()].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}

function config(){
    console.log("config called")
    max=hot1.countRows()-1
    start=$('#startn').val()
    end=$('#endn').val()
    $('#endn').attr('max', max)
    $('#startn').attr('max', max)
    $('#startn').attr('min', 0)
    $('#endn').attr('min', start)
    $('#startn').attr('min', 0)
    $('#endn_label').html("End at Row: "+end)
    $('#startn_label').html("Start at Row: "+start)
}


//init function
function init() {
    listener_table([hot1],[config])
    listener_configure(["#startn","#endn"],[config])


    max=hot1.countRows()-1
    $('#startn').attr('value', Math.round(max*0.3))
    $('#endn').attr('value', Math.round(max*0.7))
    config()
    tool()
}