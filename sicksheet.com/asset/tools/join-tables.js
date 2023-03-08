function tool() {
    data1 = hot1.getData()
    data2 = hot2.getData()
    colheader1 = data1[0]
    colheader2 = data2[0]
    key1 = colheader1[0]
    key2 = colheader2[0]

    if (key1 == key2) {
        //good, all inputs are valid
        $("#leftalert").hide()
        $("#jointype,#download").prop("disabled", false)
        $("#title3, #title4").removeClass("text-muted")
        setColorRow(hot1)
        setColorRow(hot2)
    } else {
        //some inputs are invalid
        $("#leftalert").show()
        $("#jointype,#download").prop("disabled", true)
        $("#title3,#title4").addClass("text-muted")
        $("#leftalert").html("Key Error: The first columns must have the same name. <b>" + key1 + " ≠ " + key2 + "</b>")
        setColorRow(hot1, color2)
        setColorRow(hot2, color2)
        setColorRow(hot3, color2)
        return
    }

    data1.shift()
    data2.shift()
    jointype = $("#jointype").val()
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = new dfjs.DataFrame(data2, colheader2)
    df3 = df1.join(df2, key1, jointype)
    datawithcol = [df3.listColumns()].concat(df3.toArray())
    data_to_hot("#table3",datawithcol)
    setColorRow(hot3, color1)
}

function showjoinimg() {
    jointype = $("#jointype option:selected").val()
    $("#joinimg").attr("src", "asset/img/" + jointype + ".svg")
}

function init() {
    listener_table([hot1,hot2])
    $('#jointype').change(function() {
        showjoinimg()
        tool()
    })

    $('#jointype').html("")
    $('#jointype').append('<option value="left">Left Join</option>')
    $('#jointype').append('<option value="right">Right Join</option>')
    $('#jointype').append('<option value="inner">Inner Join</option>')
    $('#jointype').append('<option value="outer">Outer Join</option>')
    $("#leftalert").hide()
    showjoinimg()
    tool()
}