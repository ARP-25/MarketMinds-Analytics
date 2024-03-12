// Initialisierung von Stripe und dessen Elementen
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);

var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card');
card.mount('#card-element');

// Referenz auf das Formular und den Ladebildschirm
var form = document.getElementById('payment-form');
var loadingOverlay = document.getElementById('loading-overlay');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    // Anzeigen des Ladebildschirms
    loadingOverlay.style.display = 'block';

    var fullName = form.querySelector('input[name="full_name"]').value;
    var email = form.querySelector('input[name="email"]').value;

    stripe.createPaymentMethod({
        type: 'card',
        card: card,
        billing_details: {
            name: fullName,
            email: email
        }
    }).then(function(result) {
        if (result.error) {
            // Fehlermeldung anzeigen
            console.log(result.error.message);
            // Verstecken des Ladebildschirms
            loadingOverlay.style.display = 'none';
        } else {
            // Erstellen eines versteckten Eingabefelds für die Payment Method ID
            var paymentMethodInput = document.createElement('input');
            paymentMethodInput.setAttribute('type', 'hidden');
            paymentMethodInput.setAttribute('name', 'payment_method_id');
            paymentMethodInput.setAttribute('value', result.paymentMethod.id);
            form.appendChild(paymentMethodInput);

            // Absenden des Formulars
            form.submit();
        }
    });
});
