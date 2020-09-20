(function($){
  $(function(){

    $('.sidenav').sidenav();

  }); // end of document ready
})(jQuery); // end of jQuery name space

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems, {
      direction: 'left'
    });
  var element = document.querySelectorAll('.carousel');
  options = {
    indicators : true,
    dist : -50,
  }
  var instances = M.Carousel.init(element, options);
  });
  elements = document.getElementsByClassName('navlinks')
  for(const element of elements){
      element.addEventListener('mouseover', ()=>{
      element.setAttribute('class', 'grey darken-2');
    })
  }
  for(const element of elements){
  element.addEventListener('mouseout', ()=>{
      element.setAttribute('class', '');
    })
  }