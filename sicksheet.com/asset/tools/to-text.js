function tool() {
    df=hot_to_dataframe(hot1)
    result=df.toCSV(header=true)
    console.log(result)
    $("#mycode").html("")
    $("#mycode").html(result)
}

function init() {
    listener_table([hot1])
    tool()
}