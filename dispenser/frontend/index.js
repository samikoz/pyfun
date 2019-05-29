const express = require('express');
const {check, validationResult} = require('express-validator/check');
const fetch = require('node-fetch');

const app = express();

app.set('views', './templates');
app.set('view engine', 'whiskers');

app.use(express.static('static_files'));

app.get('/validate', [
    check('amount').isFloat({min: 0, locale: 'en-GB'})
], (req, res) => {
    let errors = validationResult(req);
    // make index.html into a template
    // the same as it is now but with a field to invoke reddenForm method
    // normally the template is rendered without it
    // unless it's rendered from inside here
    if (! errors.isEmpty()) {
        return res.status(422).json({
            amount: req.query.amount,
            errors: errors.array()
        });
    }
    res.redirect(`/dispensed?amount=${req.query.amount}`);
});

app.get('/dispensed', (req, res) => {
    // for now it only returns response
    // will have to generate some template-html here
    const amountToDispense = req.query.amount;
    const dispenseEndpoint = process.env.DISPENSE_ENDPOINT;
    fetch(`${dispenseEndpoint}?amount=${amountToDispense}`)
    .then(backendResponse => {
        res.status(backendResponse.status);
        return backendResponse.text();
    })
    .then(res.send.bind(res)) // https://stackoverflow.com/questions/41801723/express-js-cannot-read-property-req-of-undefined
    .catch(requestError => {
        fetch('http://localhost:8000/dispense-error', {
            headers: {
                errorMessage: requestError
            }
        })
        .then(errorResponse => errorResponse.text())
        .then(res.send.bind(res));
    });
});

app.get('/dispense-error', (req, res) => {
   res.render('failed-dispense', {
       errorMessage: req.get('errorMessage')
   });
});

app.listen(process.env.APP_PORT);
