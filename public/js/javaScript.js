function changeCheck(ch,destId) {
	if (ch.checked)
		{
    document.getElementById(destId).value = '1';
		}
	else
		{
		 document.getElementById(destId).value = '0';
		}
}

function changeEnum(ch,destId) {
	if (ch.checked)
		{
    document.getElementById(destId).value = ch.value;
		}
	else
		{
		 document.getElementById(destId).value = ch.value;
		}
}

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#preview')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}



