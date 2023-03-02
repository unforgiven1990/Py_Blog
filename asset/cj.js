

$(document).ready(function() {
try{
var spy = new ScrollSpy()
var indicator = document.getElementById('indicator')
spy.Indicator({
  element: indicator
})

var spy = new ScrollSpy({
    delay: 10
})
}catch{
}

})