var press=0
function boton(){

if(press==0){
press=press+1;
input=document.getElementById("def");
input.setAttribute("style",'display:block');
}else{
press=0;
input=document.getElementById("def");
input.setAttribute("style",'display:none');
}
}

function random(){
var input
input=document.getElementById("rand");
input.click();
}
