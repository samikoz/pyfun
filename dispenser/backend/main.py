from flask import Flask, request
from flask_cors import CORS

from notes import NotePLN
from dispenser import SingleCurrencyDispenser

app = Flask('dispenser')
CORS(app)

dispenser = SingleCurrencyDispenser({
    NotePLN(100): 10**5,
    NotePLN(50): 10**5,
    NotePLN(20): 10**5,
    NotePLN(10): 10**5
})


@app.route('/dispense')
def dispense():
    amount: float = float(request.args['amount'])
    try:
        return str(dispenser.dispense(amount))
    except ValueError as e:
        return (e.args[0], 500, ())
