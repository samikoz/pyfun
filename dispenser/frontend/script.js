function sanitiseEnteredAmount() {

}

function clearEnteredAmount() {

}

function replaceDispensedAmount() {

}

document.getElementById('send_button').addEventListener('click', function() {
    var amount_to_dispense = document.getElementById('dispense_field').value;
    // get endpoint from the environment
    fetch('http://localhost:5000/dispense/' + `${amount_to_dispense}`).then(response => {
        if (response.ok) {
            return response.text();
        }
    }).then(dispensedText => {
        var dispensedTextNode = document.createTextNode(dispensedText);
        document.getElementById('dispensed').appendChild(dispensedTextNode);
    })
});