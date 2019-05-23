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
    const backendEndpoint = 'http://0.0.0.0:5000/dispense';
    const amountToDispense = req.query.amount;
    fetch(`${backendEndpoint}?amount=${amountToDispense}`, {
        'headers': {
            'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Host': 'localhost:5000',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
    })
    .then(backendResponse => {
        res.status(backendResponse.status);
        return backendResponse.text();
    })
    .then(responseText => res.send(responseText))
    .catch(err => res.send(err));
    // catch - test with non-working backend
    // error template here - could not connect to the dispensing module
    // and below the exact details
});

app.listen(port);
