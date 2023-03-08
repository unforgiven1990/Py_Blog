function tool() {

    df = hot_to_dataframe(hot1)
    column = $("#column option:selected").val()
    operation=$("#operation option:selected").val()
    df=df.groupBy(column).aggregate(group => group.stat.mean)
    datawithcol = [].concat(df.values)

    /*
    df = hot_to_dataframe(hot1).unique(uniquecol)
    datawithcol = [df.listColumns()].concat(df.toArray())
    colindex = colheader1.indexOf(sortcol)
    setColorRow(hot2, color1, colindex)
    */

    data_to_hot("#table2",datawithcol)

    //add little highlight to indicate the swapped result

}


function config(){
    columns = hot1.getData()[0]
    $('#column').html("")
    $.each(columns, function(index, val) {
        $('#column').append('<option value="' + val + '">Smallest value in column ' + val + '</option>')
    })

    a_operations={"count":"Count Occurence","sum":"Sum","std":"Standard Variation","var":"Variance","mean":"Mean","cumSum":"Cummulative Sum","cumMax":"Cummulative Max","cumProd":"Cummulative Multiplication","cummin":"Cummulative Min","max":"Maximum",'min':"Minimum"}
    $('#operation').html("")
    $.each(a_operations, function(f_name, explainer) {
        $('#operation').append('<option value="df.' + f_name + '()">' + explainer + '</option>')
    })

}


function init() {



    listener_table([hot1],[config])
    listener_configure(["#column","#operation"])
    config()

    //one time call
    var lastValue = $('#column option:last-child').val()
    $("#column").val(lastValue)
    $("#column").trigger("change")
    tool()
}