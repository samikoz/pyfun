const express = require('express');
const {check, validationResult} = require('express-validator/check');
const fetch = require('node-fetch');

const app = express();
const port = 8000;

app.use(express.static('static_files'));

app.get('/validate', [
    check('amount').isFloat({min: 0, locale: 'en-GB'})
], (req, res) => {
    let errors = validationResult(req);
    if (! errors.isEmpty()) {
        return res.status(422).json({
            amount: req.query.amount,
            errors: errors.array()
        });
    }
    res.status(200).json({amount: req.query.amount});
});

app.get('/dispensed', (req, res) => {
    // for now it only returns response
    // will have to generate some template-html here
    const backendEndpoint = 'http://127.0.0.1:5000/dispense/';
    const amountToDispense = req.query.amount;
    fetch(`${env.backendEndpoint}?amount=${amountToDispense}`)
    .then(backendResponse => {
        res.status(backendResponse.status);
        return backendResponse.text();
    })
    .then(responseText => res.send(responseText))
    .catch(err => console.log(`Error:  + ${err}`));
    // catch - test with non-working backend & failed response
});

app.listen(port);
