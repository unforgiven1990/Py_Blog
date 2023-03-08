function exampletool(){
return  {
"#table1": [

         ["1", "22", "31"],
         ["77", "22", "55"],
         ["66", "2", "111"],
         ["1111", "8", "999"],
         ["-2", "81", "72"],
    ]
}
}


function rank2DArray(arr, axis) {
  const ranks = [];
  const n = arr.length;
  const m = arr[0].length;
  if (axis === 'x') {
    for (let i = 0; i < n; i++) {
      const row = arr[i];
      const sortedRow = row.slice().sort((a, b) => a - b);
      const rankRow = row.map((x) => sortedRow.indexOf(x) + 1);
      ranks.push(rankRow);
    }
  } else if (axis === 'y') {
    console.log("y axis")
    for (let j = 0; j < m; j++) {
      const col = [];
      for (let i = 0; i < n; i++) {
        col.push(arr[i][j]);
      }
      const sortedCol = col.slice().sort((a, b) => a - b);
      const rankCol = col.map((x) => sortedCol.indexOf(x) + 1);
      for (let i = 0; i < n; i++) {
        if (!ranks[i]) {
          ranks[i] = [];
        }
        ranks[i][j] = rankCol[i];
      }
    }
  } else {
    throw new Error('Invalid axis');
  }
  return ranks;
}

function myrank(arr,asc){
var sorted = arr.slice().sort(function(a,b){return a-b})
var ranks = arr.map(function(v){ return sorted.indexOf(v)+1 })
return ranks
}

function percentileRank(arr) {
  const sortedArr = arr.slice().sort((a, b) => a - b);
  const n = sortedArr.length;
  const ranks = new Array(n);
  for (let i = 0; i < n; i++) {
    let rank = 0;
    for (let j = 0; j < n; j++) {
      if (sortedArr[j] <= arr[i]) {
        rank++;
      } else {
        break;
      }
    }
    ranks[i] = rank / n * 100;
  }
  return ranks;
}

function rankings(arr,asc,percent) {
  if (asc=="true"){
        sorted = [...arr].sort((a, b) => b - a)
  }else{
       sorted = [...arr].sort((a, b) => a-b)
  }
  if (percent=="true"){
    return arr.map((x) => Math.round(((sorted.indexOf(x) + 1)/sorted.length)*100)+"%" )
  }else{
    return arr.map((x) => sorted.indexOf(x) + 1)
  }

}

function transpose(matrix) {
  return matrix[0].map((col, i) => matrix.map(row => row[i]))
}


function tool() {
    axis = $("#axis option:selected").val()
    order = $("#order option:selected").val()
    percent = $("#percent option:selected").val()
    maxrows= hot1.countRows()
    maxcols= hot1.countCols()
    result=[[],[]]
    data=hot1.getData()

    if (axis=='x'){
        console.log("axis x")
        for (i=0;i<maxrows;i++){
            result[i]=rankings(data[i],order,percent)
        }

    }else{
        console.log("axis y")
        data=transpose(data)
        for (i=0;i<maxcols;i++){
            result[i]=rankings(data[i],order,percent)
        }
        result=transpose(result)

    }

    datawithcol =result
    data_to_hot("#table2",datawithcol)
}

function init() {
    listener_table([hot1])
    listener_configure(["#axis","#order","#percent"])

    //one time call
    $('#axis').append('<option value="y">Column-wise</option>')
    $('#axis').append('<option value="x">Row-wise</option>')

    $('#order').append('<option value="false">Ascending</option>')
    $('#order').append('<option value="true">Descending</option>')

    $('#percent').append('<option  value="false">No</option>')
    $('#percent').append('<option  value="true">Yes</option>')

    tool()
}