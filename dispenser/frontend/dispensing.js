var send_button = document.getElementById('send_button')
send_button.addEventListener('click', dispenseGivenAmount);

function dispenseGivenAmount() {
    fetchDispensedNotes(getRequestedAmount())
    .then(getResponseContentIfOk)
    .then(printDispensedNotes);
}

function fetchDispensedNotes(amount_to_dispense) {
    return fetch(`${DISPENSE_BACKEND_ENDPOINT}${amount_to_dispense}`);
}

function getRequestedAmount() {
    return document.getElementById('dispense_field').value;
}

function getResponseContentIfOk(response) {
    if (response.ok) {
        return response.text();
    }
}

function printDispensedNotes(notes) {
    var dispensedTextNode = document.createTextNode(notes);
    document.getElementById('dispensed').appendChild(dispensedTextNode);
}

function sanitiseEnteredAmount() {

}

function clearEnteredAmount() {

}

function replaceDispensedAmount() {

}