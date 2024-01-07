
// Dropdown Menu for Profile Icon
$(document).ready(function(){
    $("#dropdownMenu").click(function(event){     
        event.stopPropagation(); 
        $("#myDropdown").toggleClass("show");
    });

    $(document).on("click", function(event){       
        if (!$(event.target).closest("#dropdownMenu").length && !$(event.target).closest("#myDropdown").length) {
            $("#myDropdown").removeClass("show");
        }
    });
});

