from flask import Flask
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


@app.route('/dispense/<float:amount>')
def dispense(amount: float):
    return str(dispenser.dispense(amount))
