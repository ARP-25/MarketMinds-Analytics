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

$(document).ready(function(){
    document.addEventListener("DOMContentLoaded", function() {
        const cancelBtn = document.querySelector(".cancel-subscription");
        const confirmationDialog = document.getElementById("confirmation-dialog");

        cancelBtn.addEventListener("click", function() {
            console.log("Test")
        });

    });
});
console.log("test")