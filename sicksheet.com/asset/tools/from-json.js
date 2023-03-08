function tool() {
    df=hot_to_dataframe(hot1)
    $("#mycode").html("")
    json=df.toJSON()
    //json=JSON.stringify(json,null, "\t") // Indented with tab
    $("#mycode").html(json)
}

function init() {
    listener_table([hot1])
    tool()
    download_text(filename="data.json")
}


