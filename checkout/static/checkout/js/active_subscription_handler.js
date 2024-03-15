
var activeSubscriptionPlan_ids = JSON.parse($('#id_active_subscription_plan').text());
activeSubscriptionPlan_ids.forEach(function(id, index, array) {
    array[index] = parseInt(id, 10);
});
var elementsWithDataItemId = $('div[data-item-id]');
var newSubscriptionPlan_ids = [];
elementsWithDataItemId.each(function() {
    var itemId = $(this).data('item-id');
    newSubscriptionPlan_ids.push(itemId);
});
var id_matches = [];
activeSubscriptionPlan_ids.forEach(function(id) {
    if (newSubscriptionPlan_ids.includes(id)) {
        id_matches.push(id);
    }
});

$('div[data-item-id]').each(function() {
    var itemId = $(this).data('item-id');    
    if (id_matches.includes(itemId)) {
        $(this).addClass('already-subscribed-container mb-2');
        var alreadySubscribedDiv = $('<div>', {
            class: 'already-subscribed',
            html: "You've got active subscription time for this Plan.<br>For more Information check"
        });        
        var profileUrl = $('#dynamic_profile_url').data('url');
        var anchorProfileUrl = $('<a>', {           
            href: profileUrl,
            text: 'Profile Info'
        });
        var lineBreak = document.createElement('br');               
        var checkoutAdjsutUrl = 'adjust/' + itemId + '/';      
        var anchorAdjustUrl = $('<a>', {           
            href: checkoutAdjsutUrl,
            text: 'Remove this Plan '
        });
        var trashIcon = $('<i>', {
            class: 'fas fa-trash-alt'
        });
        anchorAdjustUrl.append(trashIcon);
        alreadySubscribedDiv.append(' ', anchorProfileUrl, '.', lineBreak, 'To proceed with checkout click ', anchorAdjustUrl, '.');
        $(this).append(alreadySubscribedDiv);
    }
});

if(id_matches != 0){
    $('#submit-button').prop('disabled', true);
}

