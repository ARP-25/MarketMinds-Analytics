$(document).ready(function(){
    console.log("Document ready!");
    $("#dropdownMenu").click(function(event){
        console.log("DropdownMenu clicked!");
        event.stopPropagation(); 
        $("#myDropdown").toggleClass("show");
    });

    $(document).on("click", function(event){
        console.log("Document clicked!");
        if (!$(event.target).closest("#dropdownMenu").length && !$(event.target).closest("#myDropdown").length) {
            $("#myDropdown").removeClass("show");
        }
    });
});

