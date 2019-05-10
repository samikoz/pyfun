const send_button = document.getElementById('send_button');
send_button.addEventListener('click', dispenseGivenAmount);

function dispenseGivenAmount() {
    validate(getRequestedAmount())
    .then(replaceRequestedAmountWithValidated)
    .then(navigateToDispensedPage())
    .catch(reddenForm)
}

function validate() {
    const validation_endpoint = 'localhost:8000/validate';
    return fetch(validation_endpoint);
    // logic rejecting promise when validation failed
    // probably with getResponseContentIfOk
}

function getResponseContentIfOk(response) {
    if (response.ok) {
        return response.text();
    }
}

function getRequestedAmount() {
    return document.getElementById('requested_amount').value;
}

function replaceRequestedAmountWithValidated(validated) {
}

function navigateToDispensedPage() {
}

function reddenForm() {
}