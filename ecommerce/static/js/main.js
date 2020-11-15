const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

const plusMinusButton = document.getElementById('plus-minus-button');
const plusMinusIcon = document.getElementById('plus-minus');
plusMinusButton.addEventListener('click', ()=>{
  if(plusMinusIcon.className == 'fas fa-plus'){
    plusMinusIcon.setAttribute('class', 'fas fa-minus');
  }else{
    plusMinusIcon.setAttribute('class', 'fas fa-plus');
  }
});

$(function(){
  $('#demo').multiselect();
});


function sticky_relocate() {
  var window_top = $(window).scrollTop();
  var footer_top = $("#footer").offset().top;
  var div_top = $('#sticky-anchor').offset().top;
  var div_height = $("#sticky").height();
  
  if (window_top + div_height > footer_top)
      $('#sticky').removeClass('stick');    
  else if (window_top > div_top) {
      $('#sticky').addClass('stick');
  } else {
      $('#sticky').removeClass('stick');
  }
}

$(function () {
  $(window).scroll(sticky_relocate);
  sticky_relocate();
});