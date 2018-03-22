var API_ENDPOINT = "https://bhafzvkso6.execute-api.us-east-1.amazonaws.com/dev"

document.getElementById("run").onclick = function() {

  var inputData = {
    "language": $('#LanguageSelected option:selected').val(),
    "text": $('#postText').val(),
    "username": $('#username').val(),
    "prog_name": $('#prog_name').val()
  };

  $.ajax({
    url: API_ENDPOINT,
    type: 'POST',
    data: JSON.stringify(inputData),
    contentType: 'application/json; charset=utf-8',
    success: function(response) {
	    //alert(response);
	//document.getElementById("postIDreturned").textContent = "Output: " + response;
	//document.getElementById("postIDreturned").innerhtml = response;
	document.getElementById("output").innerHTML = response;
	    //window.alert(response);
    },
    error: function() {
      alert("error");
    }
  });
}
function toggleTextArea() {
	var theForm = document.form1;
	var theCheck = theForm.checkbox;
	var theTextArea = theForm.textfield;
	if(theCheck.checked == true) {
		theTextArea.style.display = "block";
	} else {
		theTextArea.style.display = "none";
	}
}
document.getElementById("postText").onkeyup = function() {
  var length = $(postText).val().length;
  document.getElementById("charCounter").textContent = "Characters: " + length;
}
