// Dynamically changes the Action Attribute of .confirmCancleForm in Confirm Cancelation Modal
$('.cancelSubscriptionBtn').on('click', function() {
    var subscriptionId = $(this).data('subscription-id');
    var dynamicUrl = "cancel-subscription/"+subscriptionId+"/";
    $('.confirmCancleForm').attr('action', dynamicUrl);
});

