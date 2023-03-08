


function exampletool(){
return  {
"#table1": [

        [1, 2, 3],
        [2, 2, 3],
        [3, 2, 3],
        [4, 2, 3],
    ],

"#table2": [
        [1, 2, 3,4],
        [2, 2, 3,4],
        [3, 2, 3,4],
    ],
}
}

function tool() {
    data1 = hot1.getData()
    data2 = $("#table2").handsontable('getInstance').getData()
    console.log("data2",data2)

    df1=new dfjs.DataFrame(hot1.getData())
    df2=new dfjs.DataFrame(hot2.getData())
    df3 = df1.matrix.dot(df2)
    datawithcol = [].concat(df3.toArray())
    data_to_hot("#table3",datawithcol)
}


function init() {
    hot1.updateSettings({
        //readOnly: true, // make table cells read-only
        type: "numeric",
        format: '0.00',
    })

    hot2.updateSettings({
        //readOnly: true, // make table cells read-only
        type: "numeric"
    })

    listener_table([hot1,hot2])
    tool()
}