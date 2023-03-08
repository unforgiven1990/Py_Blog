function tool() {
    df=hot_to_dataframe(hot1,col=true)
    result=[[],[]]
    delimiter=$('#delimiter').val()
    space=$('#space').val()
    data=hot1.getData()
    maxrow=hot1.countRows()
    maxcol=hot1.countCols()
    transposed = data[0].map((_, colIndex) => data.map(row => row[colIndex]))
    for (i=0; i<maxrow; i++) {
        result[i]=new Array(maxcol)
    }

    //$.each(df.listColumns(), function(counter, val) {
    for (i=0; i<maxrow; i++) {
        for (j=0; j<maxcol; j++) {
            //join text from the previous columns together
            try{
                subarray=transposed[j].slice(0,i+1)
                result[i][j]=subarray.join(delimiter+space)
            }catch{

            }

        }
    }

    datawithcol = result
    data_to_hot("#table2",datawithcol)
}

function init() {
    listener_table([hot1])
    listener_configure(["#delimiter","#space"])
    //todo add vertical and horizontal option

     $('#delimiter').html("")
    $('#delimiter').append('<option value=",">Comma ,</option>')
    $('#delimiter').append('<option value="; ">Semicolon ;</option>')
    $('#delimiter').append('<option value="-">Minus Sign -</option>')
    $('#delimiter').append('<option value="+">Minus Plus +</option>')
    $('#delimiter').append('<option value="_">Underscore _</option>')
    $('#delimiter').append('<option value="*">Star *</option>')
    $('#delimiter').append('<option value=".">Dot .</option>')
    $('#delimiter').append('<option value="·">Interpunct ·</option>')
    $('#delimiter').append('<option value=" ">Space </option>')
    $('#delimiter').append('<option value="  ">Tab   </option>')
    $('#delimiter').append('<option value="\n">New Line</option>')

    $('#space').append('<option value=" ">Yes</option>')
    $('#space').append('<option value="">No</option>')
    tool()
}