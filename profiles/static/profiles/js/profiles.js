document.addEventListener('DOMContentLoaded', function() {
    // Dynamically changes the Action Attribute of .confirmCancleForm in Confirm Cancelation Modal
    $('.icon-trigger').on('click', function() {
        var subscriptionId = $(this).data('subscription-id');
        var dynamicUrl = "cancel-subscription/" + subscriptionId + "/";
        $('.confirmCancleForm').attr('action', dynamicUrl);
    });
    // Dynamically changes the Action Attribute of .confirmRenewForm in Confirm Renewal Modal
    $('.icon-renew-trigger').on('click', function() {
        var subscriptionId = $(this).data('subscription-id');
        var dynamicUrl = "initiate-subscription-renewal/" + subscriptionId + "/";
        $('.confirmRenewForm').attr('action', dynamicUrl);
    });

    // Autorefresh Site on redirect for icon update after renewal or cancellation
    var url = new URL(window.location.href);
    var params = new URLSearchParams(window.location.search);
    if (params.has('refreshed')) {
        console.log("'refreshed' parameter found. Reloading page after 1 second delay.");
    
        // Delayed reload
        setTimeout(function() {
            params.delete('refreshed');
            url.search = params;
            window.history.replaceState({}, '', url);
            window.location.reload(true);
        }, 1000); // Delay for 1 second (1000 milliseconds)
    } else {
        console.log("'refreshed' parameter not found.");
    }
});



