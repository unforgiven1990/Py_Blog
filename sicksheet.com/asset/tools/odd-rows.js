function tool() {
    data=hot1.getData()
    datawithcol = result = data.filter((a,i) => i%2-1===0)
    datawithcol.unshift(data[0])//needed in order to add labels
    data_to_hot("#table2",datawithcol)
}


//init function
function init() {
    listener_table([hot1])
    listener_configure(["#n"])

    tool()
}