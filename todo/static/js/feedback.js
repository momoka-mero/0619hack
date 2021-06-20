window.onload = function() {
    popupImage();
    // var ok = document.getElementById('ok');
    // var mymodal=document.getElementById('mymodal')
    // mymodal.style.opacity=0;
    // mymodal.style.pointerEvents="none";
    
    // ok.addEventListener('click', function(){
    //     console.log("ok")
    //     mymodal.style.opacity=0.7;
    //     mymodal.style.pointerEvents="auto";
    //     mymodal.classList.toggle('is-show');
    // });
}
function popupImage() {
    console.log("poupu")
    var popup = document.getElementById('js-popup');
    if(!popup){
        console.log("popup not found")
        return;
    }
  
    var blackBg = document.getElementById('js-black-bg');
    var closeBtn = document.getElementById('js-close-btn');
    var showBtn = document.getElementById('js-show-popup');
  
    closePopUp(blackBg);
    closePopUp(closeBtn);
    closePopUp(showBtn);
    function closePopUp(elem) {
      if(!elem) {
          console.log("elem")
          return;
        }
      elem.addEventListener('click', function() {
          console.log("click")
          popup.classList.toggle('is-show');
      });
    }
  }
 
// let button=document.getElementById("ok");
// button.innerHTML="button"
// button.addEventListener("click",function(){
//     let mymodal=document.getElementbyId("mymodal");
//     mymodal.opacity=1;
// })