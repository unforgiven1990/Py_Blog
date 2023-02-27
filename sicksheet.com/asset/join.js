$(document).ready(function() {
    d_data={
    "#table1": [
            ['Name', 'Age','Car Brand'],
            ['Ali', "20","NIO"],
            ['Max', "33","Tesla"],
            ['James', "27","BMW"],
            ['Jane', "25","Mercedes"],
          ],
    "#table2": [
             ['Name', 'Country', 'Height'],
            ['Ali', "Italy", "1.7"],
            ['Eric', "USA", "1.8"],
            ['Jane', "Germany", "1.6"],
            ['Anna', "Japan", "1.7"],
          ],
    "#table3": [],
    }

    d_readonly={
        "#table1":false,
        "#table2":false,
        "#table3":true,
    }

    function init(data){
        return {
              data: data,
              rowHeaders: true,
              colHeaders: true,
              contextMenu: true,
              readOnly: false,
              renderAllRows: false,
              manualRowMove: true,
              manualColumnMove: true,
              colWidths: 100,
              width: '100%',
              height: 150,
              viewportColumnRenderingOffset:5,
              viewportRowRenderingOffset:5,
              licenseKey:'non-commercial-and-evaluation'
            }
    }

    for(let [index, item] of ["#table1","#table2","#table3"].entries() ){
        $(item).handsontable(init(data=d_data[item]))
    }

    //set color of table 1 and 2
    function setColor(hot, color="#fff"){
        var rows=hot.countRows();  // get the count of the rows in the table
        for(var row=0; row<rows; row++){  // go through each row of the table
                var cell = hot.getCell(row,0);
                cell.style.background = color;
        }
    }

    function myjoin(){
        //get data
        data1=hot1.getData()
        data2=hot2.getData()
        colheader1=data1[0]
        colheader2=data2[0]
        //check if they have first column
        //check if the first column is called same
        key1=colheader1[0]
        key2=colheader2[0]

        if (key1==key2){
            //good, all inputs are valid
            $("#leftalert").hide()
            $("#jointype").prop("disabled", false)
            $("#download").prop("disabled", false)
            $("#title3").removeClass("text-muted")
            $("#title4").removeClass("text-muted")
            setColor(hot1)
            setColor(hot2)
        }else{
            //some inputs are invalid
            $("#leftalert").show()
            $("#jointype").prop("disabled", true)
            $("#download").prop("disabled", true)
            $("#title3").addClass("text-muted")
            $("#title4").addClass("text-muted")
            $("#leftalert").html("Key Error: The first columns must have the same name. <b>"+key1+" ≠ "+key2+"</b>")
            setColor(hot1, "#f8d7da")
            setColor(hot2, "#f8d7da")
            setColor(hot3, "#f8d7da")
            return
        }

        data1.shift()
        data2.shift()
        jointype=$("#jointype").val()

        //do with data-forge-ts
        df1 = new dfjs.DataFrame(data1, colheader1)
        df2 = new dfjs.DataFrame(data2, colheader2)
        df3=df1.join(df2, key1, jointype)
        datawithcol=[df3.listColumns()].concat(df3.toArray())

        //create table
        $("#table3").handsontable(init(data=datawithcol))
        hot3 =$("#table3").handsontable('getInstance')
        hot3.updateSettings({
        //readOnly: true, // make table cells read-only
        editor: false
        });
        setColor(hot3)
    }

    function showjoinimg(){
        //depending on what join type is selected, show related image
        jointype = $("#jointype option:selected").val()
        $("#joinimg").attr("src", "asset/"+jointype+".svg")
    }



    function downloadCSV(){
        //doenst work yet
        var str = encodeURIComponent($('div[id$=table3] > .ht_master').html())
        var uri = 'data:text/csv;charset=utf-8,' + str;

        var downloadLink = document.createElement("a");
        downloadLink.href = uri;
        downloadLink.download = "joined.csv";

        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    }

    function downloadEXCEL(){
        window.open('data:application/vnd.ms-excel' + encodeURIComponent($('div[id$=table3] > .ht_master').html() )  );
    }


    //init function
    hot1 =$("#table1").handsontable('getInstance')
    hot2 =$("#table2").handsontable('getInstance')
    hot3 =$("#table3").handsontable('getInstance')

    hot1.addHook('afterChange', (row, amount) => {
        myjoin()
    })

    hot2.addHook('afterChange', (row, amount) => {
        myjoin()
    })

    $('#jointype').change(function() {
        showjoinimg()
        myjoin()
    })

    $("#step1tooltip, #step2tooltip, #step3tooltip, #step4tooltip").tooltip()
    $("#leftalert").hide()
    myjoin()
    showjoinimg()
    setColor(hot1)
    setColor(hot2)

    //setup download button
    const exportPlugin = hot3.getPlugin('exportFile')
    const button = document.querySelector('#download')
    button.addEventListener('click', () => {
        exportPlugin.downloadFile('csv', {
        bom: false,
        columnDelimiter: ',',
        columnHeaders: false,
        exportHiddenColumns: true,
        exportHiddenRows: true,
        fileExtension: 'csv',
        filename: $("#jointype option:selected").text()+'_[YYYY]-[MM]-[DD]',
        mimeType: 'text/csv;charset=utf-8,',
        rowDelimiter: '\r\n',
        rowHeaders: true
        })
    })

})