function tool() {
    var DataFrame = dfjs.DataFrame
    data=$("#mycode").val()
    result=[]
    $.each(data.split("\n"), function(counter1, row) {
            len=row.split(',').length
            result[counter1]= new Array(len)
     })

    //split by \n and ,
     $.each(data.split("\n"), function(counter1, row) {
         $.each(row.split(','), function(counter2, cell) {
            result[counter1][counter2]=cell
         })
     })

    df=new DataFrame(result)
    datawithcol = [].concat(df.toArray())
    data_to_hot("#table2",datawithcol)
}

function init() {
    listener_configure(["#mycode"],[],event="input")
    $("#mycode").html("Name,Age,Car Brand\nAli,20,NIO\nMax,33,Tesla\nJames,27,BMW\nJane,25,Mercedes")
    tool()
}


