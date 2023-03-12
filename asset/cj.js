

$(document).ready(function() {

//google analytics
try{
 window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-P51XXPEYHZ');

}catch{}



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