$(document).ready(function() {


    function tool(){
        //get data
        data1=hot1.getData()

        //do with data-forge-ts
        df1 = new dfjs.DataFrame(data1, data1[0])
        df2=df1.transpose()
        datawithcol=[].concat(df2.toArray())

        //create table
        $("#table2").handsontable(init(data=datawithcol))
        hot2 =$("#table2").handsontable('getInstance')
        hot2.updateSettings({
        //readOnly: true, // make table cells read-only
            editor: false
        });

        //add little highlight to indicate the swapped result
        setColorColumn(hot1,color1)
        setColorIndex(hot2,color1)
    }


    //init function
    hot1 =$("#table1").handsontable('getInstance')
    hot2 =$("#table2").handsontable('getInstance')

    hot1.addHook('afterChange', (row, amount) => {
        myjoin()
    })

    tool()
    myexport(hot2,"Transposed")

})