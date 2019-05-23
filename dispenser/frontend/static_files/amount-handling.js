const selfEndpoint = 'http://localhost:8000';

const send_button = document.getElementById('send_button');
send_button.addEventListener('click', dispenseRequestedAmount);

function dispenseRequestedAmount() {
    validate(getRequestedAmount())
    .then(navigateToDispensedPage)
    .catch(reddenForm);
}

function validate(amount) {
    const validationEndpoint = `${selfEndpoint}/validate`;
    return fetch(`${validationEndpoint}?amount=${amount}`)
    .then(retrieveResponseContent);
}

function getRequestedAmount() {
    return document.getElementById('requested_amount').value;
}

function retrieveResponseContent(response) {
    if (response.ok) {
        return response.json();
    } else {
        return response.text().then(err => Promise.reject(err));
    }
}

function navigateToDispensedPage(response) {
    window.location.href = `${selfEndpoint}/dispensed?amount=${response.amount}`;
}

function reddenForm(errMsg) {
    const inputFieldID = 'requested_amount';
    switchOffTransitionProperty(inputFieldID);
    turnFormBackgroundRedAndSwitchOnTransition(inputFieldID);
    turnFormBackgroundWhite(inputFieldID);
    console.log(`Error: ${errMsg}`);
}

function switchOffTransitionProperty(elementId) {
    document.getElementById(elementId).classList.remove('transitionable');
}

function turnFormBackgroundRedAndSwitchOnTransition(elementId) {
    const element = document.getElementById(elementId);
    element.style['background-color'] = 'red';
    element.classList.add('transitionable');
}

function turnFormBackgroundWhite(elementId) {
    document.getElementById(elementId).style['background-color'] = 'white';
}
