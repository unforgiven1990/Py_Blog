function tool() {
    df=hot_to_dataframe(hot1)
    $("#mycode").html("")
    delimiter=$("#delimiter option:selected").val()
    result=df.toDSV(delimiter)//todo currently bugged implementation
    console.log(result)
    //result=JSON.stringify(result)
    $("#mycode").html(result)
}

function init() {
    listener_table([hot1])
    listener_configure(["#delimiter"])
    tool()

    $('#delimiter').html("")
    $('#delimiter').append('<option value=";">Semicolon ;</option>')
    $('#delimiter').append('<option value=",">Comma ,</option>')
    $('#delimiter').append('<option value=" ">Space </option>')
    $('#delimiter').append('<option value="  ">Tab   </option>')
    download_text(filename="data.txt")
}


