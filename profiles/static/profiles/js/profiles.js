// Dynamically changes the Action Attribute of .confirmCancleForm in Confirm Cancelation Modal
// Attach event listener to the icon/button with the class '.toggle-icon'
$('.icon-trigger').on('click', function() {
    var subscriptionId = $(this).data('subscription-id');
    console.log(subscriptionId + " is the subscription id");
    var dynamicUrl = "cancel-subscription/" + subscriptionId + "/";
    $('.confirmCancleForm').attr('action', dynamicUrl);
});


