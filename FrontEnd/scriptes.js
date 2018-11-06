function readURL(input)
{
    if (input.files && input.files[0]) 
    {
        var reader = new FileReader();

        reader.onload = function (e) 
        {
            $('#Uimage').attr('src', e.target.result).width(250).show();
            $('#drop').hide();
            $('#or').hide();
            $('#image_icon').hide();
            $('#cancel').show();
            $('#browse').hide();
        };

        reader.readAsDataURL(input.files[0]);
    }
}

/* Open */
function openNav() {
    document.getElementById("myNav").style.height = "100%";
}

/* Close */
function closeNav() {
    document.getElementById("myNav").style.height = "0%";
}

function openStatus() {
    document.getElementById("status").style.height = "100%";
    document.getElementById("progressBar").style.width = "100%";
}

/* Close */
function closeStatus() {
    document.getElementById("status").style.height = "0%";
}