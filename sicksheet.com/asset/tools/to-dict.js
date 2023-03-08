function tool() {
    df=hot_to_dataframe(hot1)
    $("#mycode").html("")
    result=df.toDict()
    result=JSON.stringify(result)
    $("#mycode").html(result)
}

function init() {
    listener_table([hot1])
    tool()
    download_text(filename="data.txt")
}


