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
