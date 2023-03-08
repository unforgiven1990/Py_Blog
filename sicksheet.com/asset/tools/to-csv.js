function tool() {
    df=hot_to_dataframe(hot1)
    $("#mycode").html("")
    $("#mycode").html(df.toCSV(header=true))
}

function init() {
    listener_table([hot1])
    tool()
    download_text(filename="data.csv")
}


