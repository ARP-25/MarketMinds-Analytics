// Dynamically changes the Action Attribute of .confirmCancleForm in Confirm Cancelation Modal
// Attach event listener to the icon/button with the class '.toggle-icon'
$('.icon-trigger').on('click', function() {
    var subscriptionId = $(this).data('subscription-id');
    console.log(subscriptionId + " is the subscription id");
    var dynamicUrl = "cancel-subscription/" + subscriptionId + "/";
    $('.confirmCancleForm').attr('action', dynamicUrl);
});
// Dynamically changes the Action Attribute of .confirmRenewForm in Confirm Renewal Modal
$('.icon-renew-trigger').on('click', function() {
    var subscriptionId = $(this).data('subscription-id');
    console.log("clicked");
    console.log(subscriptionId + " is the subscription id");
    var dynamicUrl = "initiate-subscription-renewal/" + subscriptionId + "/";
    console.log(subscriptionId + " is the subscription id");
    $('.confirmRenewForm').attr('action', dynamicUrl);
});


