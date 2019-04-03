from flask import Flask
from flask_cors import CORS

from dispenser import basic_dispenser

app = Flask('dispenser')
CORS(app)


@app.route('/dispense/<float:amount>')
def dispense(amount: float):
    return str(basic_dispenser.dispense(amount))
