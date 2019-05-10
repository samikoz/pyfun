const express = require('express')
const app = express();
const port = 8000;

// want to serve only index, without js files
app.use(express.static('static_files'));

// get? have to post the amount
app.get('validate', (res, req) => {
// https://express-validator.github.io/docs/
// ensure non-negative number
// only one comma
// trim leading zeros
// comma into dot
// remove trailing zeros after comma
})

// same here, posting validated
app.get('dispensed', (res, req) => {
// a) calls the dispensing endpoint
// function fetchDispensedNotes(amount_to_dispense) {
//     return fetch(`${DISPENSE_BACKEND_ENDPOINT}${amount_to_dispense}`);
// }
// b) depending on the validation outcome presents one of two pages,
// the successful one from some sort of template
})

app.listen(port);