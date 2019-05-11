const express = require('express');
const {check, validationResult} = require('express-validator/check');

const app = express();
const port = 8000;

app.use(express.static('static_files'));

app.get('/validate', [
    check('amount').isFloat({min: 0, locale: 'en-GB'})
], (req, res) => {
    const errors = validationResult(req);
    if (! errors.isEmpty()) {
        return res.status(422).json({
            amount: req.query.amount,
            errors: errors.array()
        });
    }
    res.status(200).json({amount: req.query.amount});
});

app.get('/dispensed', (req, res) => {
// a) calls the dispensing endpoint
// function fetchDispensedNotes(amount_to_dispense) {
//     return fetch(`${DISPENSE_BACKEND_ENDPOINT}${amount_to_dispense}`);
// }
// b) depending on the validation outcome presents one of two pages,
// the successful one from some sort of template
});

app.listen(port);