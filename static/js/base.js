// Dropdown Menu for Profile Icon
$(document).ready(function () {
    $("#dropdownMenu").click(function (event) {
        event.stopPropagation();
        $("#myDropdown").toggleClass("show");
    });
    $("#dropdownMenu").mouseenter(function (event) {
        event.stopPropagation();
        $("#myDropdown").toggleClass("show");
    });
    $("#myDropdown").mouseleave(function (event) {
        $("#myDropdown").removeClass("show");
    });
    $(document).on("click", function (event) {
        if (!$(event.target).closest("#dropdownMenu").length && !$(event.target).closest("#myDropdown").length) {
            $("#myDropdown").removeClass("show");
        }
    });

    $("#dropdownBag").mouseenter(function (event) {
        event.stopPropagation();
        $("#myDropdownBag").toggleClass("show");
        $("#myDropdown").removeClass("show");
    });
    $(document).on("click", function (event) {
        if (!$(event.target).closest("#dropdownBag").length && !$(event.target).closest("#myDropdownBag").length) {
            $("#myDropdownBag").removeClass("show");
        }
    });

});