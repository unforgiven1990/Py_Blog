
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


//set color of table 1 and 2
function setColorRow(hot, color="#fff",rowindex=0){
    var rows=hot.countRows();  // get the count of the rows in the table
    for(var row=0; row<rows; row++){  // go through each row of the table
            var cell = hot.getCell(row,rowindex);
            cell.style.background = color;
    }
}

function setColorColumn(hot, color="#fff",colindex=0){
    console.log(hot,color,colindex)
    var cols=hot.countCols();  // get the count of the rows in the table
    for(var col=0; col<cols; col++){  // go through each row of the table
            var cell = hot.getCell(colindex,col);
            cell.style.background = color;
    }
}


function myexport(hot,name){
    //setup download button
    const exportPlugin = hot.getPlugin('exportFile')
    const button = document.querySelector('#download')
    button.addEventListener('click', () => {
        exportPlugin.downloadFile('csv', {
        bom: false,
        columnDelimiter: ',',
        columnHeaders: false,
        exportHiddenColumns: true,
        exportHiddenRows: true,
        fileExtension: 'csv',
        filename: name+'_[YYYY]-[MM]-[DD]',
        mimeType: 'text/csv;charset=utf-8,',
        rowDelimiter: '\r\n',
        rowHeaders: true
        })
    })
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


 color1="#d3eaf2"
$(".mytooltip").tooltip()
for(let [index, item] of ["#table1","#table2","#table3"].entries() ){
        $(item).handsontable(init(data=d_data[item]))
}