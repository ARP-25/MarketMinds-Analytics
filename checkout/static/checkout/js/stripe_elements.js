// Assuming this is your existing Stripe setup and card element
// Initialising Stripe Element and mount it to checkout Form
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);


var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    var fullName = form.querySelector('input[name="full_name"]').value;
    var email = form.querySelector('input[name="email"]').value;

    stripe.createPaymentMethod({
        type: 'card',
        card: card,
        billing_details: {
            name: fullName,  // Retrieved from form
            email: email     // Retrieved from form
        }
    }).then(function(result) {
        if (result.error) {
            // Display error.message in your UI
            console.log(result.error.message);
        } else {
            // Create a hidden input to store the payment method ID
            var paymentMethodInput = document.createElement('input');
            paymentMethodInput.setAttribute('type', 'hidden');
            paymentMethodInput.setAttribute('name', 'payment_method_id');
            paymentMethodInput.setAttribute('value', result.paymentMethod.id);
            form.appendChild(paymentMethodInput);

            // Submit the form
            form.submit();
        }
    });
});
