$(document).ready(function () {
 
    // Dropdown Menu for Profil displaying functionality
    let canFadeOut = true;
    $("#dropdownMenu").click(function (event) {
        event.stopPropagation();
        $("#myDropdown").fadeToggle(300); 
    });
    $("#dropdownMenu").mouseenter(function (event) {
        event.stopPropagation();
        $("#myDropdown").stop(false, true).fadeIn(300); 
        $("#myDropdownBag").stop(false, true).fadeOut(300); 
        canFadeOut = false;
        setTimeout(function() {
            canFadeOut = true;
        }, 300);
    });
    $("#myDropdown").mouseleave(function (event) {
        if (canFadeOut) {
            $("#myDropdown").stop(false, true).fadeOut(300); 
        }
    });
    $(document).on("click", function (event) {
        if (!$(event.target).closest("#dropdownMenu").length && !$(event.target).closest("#myDropdown").length) {
            if (canFadeOut) {
                $("#myDropdown").stop(false, true).fadeOut(300); 
            }
        }
    });

    // Showing miniature shopping bag only when badge > 0 (badge is derived from bag_items count)
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

     // FAQ toggling answers
    $('.faq-question').click(function(){
        $(this).next('.faq-answer').slideToggle();
        $(this).find('i').toggleClass('fa-angle-down fa-angle-up');
        $('.faq-question').not(this).next('.faq-answer:visible').slideUp();
        $('.faq-question').not(this).find('i.fa-angle-up').removeClass('fa-angle-up').addClass('fa-angle-down');
    });

    // Footer Switch color of title on hover
    $('.footer-element-container').hover(
        function() {
            $(this).find('.text-secondary-custom:first').addClass('text-highlight').removeClass('text-secondary-custom');
        },
        function() {
            $(this).find('.text-highlight:first').addClass('text-secondary-custom').removeClass('text-highlight');
        }
    );

    // Hover color Effekt für Developed By Footer
    $('.footer-links').hover(
        function() {
            $(this).find('span').addClass('text-white');
            $(this).find('i').addClass('theme-color');
        }, 
        function() {
            $(this).find('span').removeClass('text-white');
            $(this).find('i').removeClass('theme-color');
        }
    );

    // Skript um Footer immer am ende vom Viewport anzuheften egal wie viel Content vorhanden ist
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













  
  
  