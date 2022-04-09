//const name = document.querySelector("#id_username");

function onClickBlue(){
	document.getElementById("id_username").style.color = "red";
	document.getElementById("id_username").style.borderColor = "red";
}

function myBlue(){
	document.getElementById("id_username").style.color = "";
	document.getElementById("id_username").style.borderColor = "";
}

var form = document.getElementById('form');

form.addEventListener("focus", onClickBlue, true);
form.addEventListener("blur", myBlue, true);

//name.addEventListener("click", myScript);
/*
const form = document.getElementById('form');

form.addEventListener('focus', (event) => {
  event.target.style.background = 'pink';
}, true);

form.addEventListener('blur', (event) => {
  event.target.style.background = '';
}, true);
*/