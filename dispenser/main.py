from flask import Flask

from dispenser import basic_dispenser

app = Flask('dispenser')


@app.route('/dispense/<float:amount>')
def dispense(amount: float):
    return str(basic_dispenser.dispense(amount))
