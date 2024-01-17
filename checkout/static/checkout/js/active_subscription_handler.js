
var activeSubscriptionPlan_ids = JSON.parse($('#id_active_subscription_plan').text());
console.log(activeSubscriptionPlan_ids)
activeSubscriptionPlan_ids.forEach(function(id, index, array) {
    array[index] = parseInt(id, 10);
});
console.log(activeSubscriptionPlan_ids);


var elementsWithDataItemId = $('div[data-item-id]');
var newSubscriptionPlan_ids = [];
elementsWithDataItemId.each(function() {
    var itemId = $(this).data('item-id');
    newSubscriptionPlan_ids.push(itemId);
});
console.log('Item IDs:', newSubscriptionPlan_ids);


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
            text: 'Already subscribed. For more Information check'
        });        
        var profileUrl = $('#dynamic_profile_url').data('url');
        var anchorElement = $('<a>', {           
            href: profileUrl,
            text: 'Profile Info'
        });        
        alreadySubscribedDiv.append(' ', anchorElement, '.');
        $(this).append(alreadySubscribedDiv);
    }
});
