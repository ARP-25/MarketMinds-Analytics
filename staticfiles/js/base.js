$(document).ready(function () {

    $("#dropdownMenu").click(function (event) {
        event.stopPropagation();
        $("#myDropdown").toggleClass("show");
    });
    $("#dropdownMenu").mouseenter(function (event) {
        event.stopPropagation();
        $("#myDropdown").toggleClass("show");
        $("#myDropdownBag").removeClass("show");
    });
    $("#myDropdown").mouseleave(function (event) {
        $("#myDropdown").removeClass("show");
    });
    $(document).on("click", function (event) {
        if (!$(event.target).closest("#dropdownMenu").length && !$(event.target).closest("#myDropdown").length) {
            $("#myDropdown").removeClass("show");
        }
    });
    if ($('span.badge').length > 0) {
        $("#dropdownBag").mouseenter(function (event) {
            event.stopPropagation();
            $("#myDropdownBag").toggleClass("show");
            $("#myDropdown").removeClass("show");
        });
    }
    $("#myDropdownBag").mouseleave(function (event) {
        $("#myDropdownBag").removeClass("show");
    });
    $(document).on("click", function (event) {
        if (!$(event.target).closest("#dropdownBag").length && !$(event.target).closest("#myDropdownBag").length) {
            $("#myDropdownBag").removeClass("show");
        }
    });

});
/* Footer */
$(document).ready(function() {
    function adjustFooter() {
      var bodyHeight = $('body').outerHeight();
      var windowHeight = $(window).height();
      if (bodyHeight > windowHeight * 0.8) {
        $('footer').addClass('footer-static');
        $('footer').removeClass('footer-absolute');
      } else {
        $('footer').removeClass('footer-static');
        $('footer').addClass('footer-absolute');
      }
    }
    adjustFooter(); 
    $(window).resize(adjustFooter);
});
  
  
  