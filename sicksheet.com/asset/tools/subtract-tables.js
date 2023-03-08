


function exampletool(){
return  {
"#table1": [

         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12],
    ],

"#table2": [
        [1, 2, 4],
        [2, 2, 3],
        [3, 2, 3],
        [4, 2, 3],
    ],
}
}

function tool() {
    //mark color what is not numeric
    //generate_numeric_config(hot1)
    //generate_numeric_config(hot2)
    if(setColorNonNumeric(hot1)){
        $("#table1_alert").show()
    }else{
        $("#table1_alert").hide()
    }

    if(setColorNonNumeric(hot2)){
        $("#table2_alert").show()
    }else{
        $("#table2_alert").hide()
    }



    data1 = hot1.getData()
    data2 = hot2.getData()
    maxrow = Math.max(hot1.countRows(), hot2.countRows())
    maxcol = Math.max(hot1.countCols(), hot2.countCols())
    nd_result =[]

    //create empty result frame
    for (var i = 0; i < maxrow; i++) {
      nd_result[i] = new Array(maxcol);
    }

    //add content to result frame
    for (let i = 0; i < maxrow; i++) {
        for (let j = 0; j < maxcol; j++) {
                cell1=data1[i][j]
                cell1 = cell1 || 0
                cell2=data2[i][j]
                cell2 = cell2 || 0
            nd_result[i][j]=cell1-cell2
        }
    }

    datawithcol = nd_result
    data_to_hot("#table3",datawithcol)
    setColorNonNumeric(hot3)
}


function generate_numeric_config(hot){
rows=hot.countRows()-1
result=[]
for (let i = 0; i < rows; i++) {
result.push({
data:i,
type: 'numeric',
format: '$0,0.00', })
}

hot.updateSettings({
    type: "numeric",
    columns: result,
    })
}




function init() {
    $("#table1_alert, #table2_alert").hide()
    listener_table([hot1,hot2])
    tool()
}