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


