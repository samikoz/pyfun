const selfEndpoint = 'localhost:8000';

const send_button = document.getElementById('send_button');
send_button.addEventListener('click', dispenseGivenAmount);

function dispenseGivenAmount() {
    validate(getRequestedAmount())
    .then(replaceRequestedAmountWithValidated)
    .then(navigateToDispensedPage())
    .catch(reddenForm)
}

function validate(amount) {
    const validation_endpoint = `${selfEndpoint}/validate``;
    fetch(`${validation_endpoint}?amount=${amount}`)
    .then(getResponseContentIfOk)
    .then(navigateToDispensedPage)
    .catch(reddenForm)
}

function getResponseContentIfOk(response) {
    if (response.ok) {
        return response.text();
    } else {
        return response.text().then(err => Promise.reject(err));
    }
}

function getRequestedAmount() {
    return document.getElementById('requested_amount').value;
}

function navigateToDispensedPage(amount) {
    window.location.href = `${selfEndpoint}/dispensed?amount=${amount}`;
}

function reddenForm(errMsg) {
    console.log(`Error: ${errMsg}`);
}