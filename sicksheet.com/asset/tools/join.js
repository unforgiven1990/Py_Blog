function tool() {
    //get data
    data1 = hot1.getData()
    data2 = hot2.getData()
    colheader1 = data1[0]
    colheader2 = data2[0]
    //check if they have first column
    //check if the first column is called same
    key1 = colheader1[0]
    key2 = colheader2[0]

    if (key1 == key2) {
        //good, all inputs are valid
        $("#leftalert").hide()
        $("#jointype").prop("disabled", false)
        $("#download").prop("disabled", false)
        $("#title3").removeClass("text-muted")
        $("#title4").removeClass("text-muted")
        setColorRow(hot1)
        setColorRow(hot2)
    } else {
        //some inputs are invalid
        $("#leftalert").show()
        $("#jointype").prop("disabled", true)
        $("#download").prop("disabled", true)
        $("#title3").addClass("text-muted")
        $("#title4").addClass("text-muted")
        $("#leftalert").html("Key Error: The first columns must have the same name. <b>" + key1 + " ≠ " + key2 + "</b>")
        setColorRow(hot1, "#f8d7da")
        setColorRow(hot2, "#f8d7da")
        setColorRow(hot3, "#f8d7da")
        return
    }

    data1.shift()
    data2.shift()
    jointype = $("#jointype").val()

    //do with data-forge-ts
    df1 = new dfjs.DataFrame(data1, colheader1)
    df2 = new dfjs.DataFrame(data2, colheader2)
    df3 = df1.join(df2, key1, jointype)
    datawithcol = [df3.listColumns()].concat(df3.toArray())

    //create table
    $("#table3").handsontable(datainit(data = datawithcol))
    hot3 = $("#table3").handsontable('getInstance')
    hot3.updateSettings({
        //readOnly: true, // make table cells read-only
        editor: false
    });
    setColorRow(hot3, color1)
}

function showjoinimg() {
    jointype = $("#jointype option:selected").val()
    $("#joinimg").attr("src", "asset/" + jointype + ".svg")
}


function init() {

    hot1.addHook('afterChange', (row, amount) => {
        tool()
    })

    hot2.addHook('afterChange', (row, amount) => {
        tool()
    })

    $('#jointype').change(function() {
        showjoinimg()
        tool()
    })

    $("#leftalert").hide()
    showjoinimg()
    tool()

}