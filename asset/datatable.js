$(document).ready(function() {
var DataFrame = dfjs.DataFrame

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


hot1 =$("#table1").handsontable('getInstance')
hot2 =$("#table2").handsontable('getInstance')
hot3 =$("#table3").handsontable('getInstance')

hot1.addHook('afterChange', (row, amount) => {
    myvalidation()
    myjoin()
})

hot2.addHook('afterChange', (row, amount) => {
    myvalidation()
    myjoin()
})

//set color of table 1 and 2
function setColor(hot, color="#fff"){
var rows=hot.countRows();  // get the count of the rows in the table
for(var row=0; row<rows; row++){  // go through each row of the table
        var cell = hot.getCell(row,0);
        cell.style.background = color;
}
}

setColor(hot1)
setColor(hot2)



function myvalidation(){
//check if they have first column
//check if the first column is called same

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
//good
$("#leftalert").hide()
$("#jointype").prop("disabled", false)
$("#download").prop("disabled", false)
$("#title3").removeClass("text-muted")
$("#title4").removeClass("text-muted")
setColor(hot1)
setColor(hot2)
}else{
//return
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


if (false){//do with danfo
df1 = new dfd.DataFrame(data1, { columns: colheader1})
df2 = new dfd.DataFrame(data2, { columns: colheader2 })
df3 = dfd.merge({ "left": df1, "right": df2, "on": [colheader1[0]], how: jointype})
datawithcol=[df3.columns].concat(df3.values)
}else{ //do with data-forge-ts
df1 = new DataFrame(data1, colheader1)
df2 = new DataFrame(data2, colheader2)
df3=df1.join(df2, key1, jointype)
datawithcol=[df3.listColumns()].concat(df3.toArray())
}





    //create table
    $("#table3").handsontable(init(data=datawithcol))
    hot3 =$("#table3").handsontable('getInstance')
    hot3.updateSettings({
    //readOnly: true, // make table cells read-only
    editor: false
    });
    setColor(hot3)


 }



$('#jointype').change(function() {
    showjoinimg()
    myjoin()
})


function showjoinimg(){
//depending on what join type is selected, show related image
jointype = $("#jointype option:selected").val()
$("#joinimg").attr("src", "asset/"+jointype+".png");
}


$("#leftalert").hide()
myjoin()
showjoinimg()





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


function downloadHOT(){

}

$("#download").click(function(e) {
    //downloadEXCEL()
});


const exportPlugin = hot3.getPlugin('exportFile');
const button = document.querySelector('#download');

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
      });
    });





//guideline starts
steps = document.querySelector("#steps");
steps = ''

let wizards = [
  {
    complete: true,
    number: 1,
    title: "Verify Identity",
    text:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat pariatur minima nemo? Facilis veniam reprehenderit quaerat aspernatur, quis voluptas voluptate."
  },
  {
    complete: false,
    number: 2,
    title: "Create Account",
    text:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat pariatur minima nemo? Facilis veniam reprehenderit quaerat aspernatur, quis voluptas voluptate."
  },
    {
    complete: false,
    number: 3,
    title: "Login",
    text:
      "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugiat pariatur minima nemo? Facilis veniam reprehenderit quaerat aspernatur, quis voluptas voluptate."
  },
];

let tickIcon = `<svg viewBox="0 0 512 512" width="100" title="check">
        <path d="M173.898 439.404l-166.4-166.4c-9.997-9.997-9.997-26.206 0-36.204l36.203-36.204c9.997-9.998 26.207-9.998 36.204 0L192 312.69 432.095 72.596c9.997-9.997 26.207-9.997 36.204 0l36.203 36.204c9.997 9.997 9.997 26.206 0 36.204l-294.4 294.401c-9.998 9.997-26.207 9.997-36.204-.001z" />`;

steps.innerHTML = wizards
  .map(function (wizard) {
    return (
      `<div class='step'>` +
      `<div class='number ${wizard.complete && 'completed'}'>` +
      (wizard.complete ? tickIcon : wizard.number) +
      `</div>` +
      `<div class='info'>` +
      `<p class='title'>${wizard.title}</p>` +
      `<p class='text'>${wizard.text}</p>` +
      "</div>" +
      "</div>"
    );
  })
  .join("");





$("#step1tooltip").tooltip()
$("#step2tooltip").tooltip()
$("#step3tooltip").tooltip()
$("#step4tooltip").tooltip()


})