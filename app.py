
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zjmvp'

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/passwordValidator", methods=['GET', 'POST'])
def password_validator():
    return render_template('passwordValidator.html')


@app.route("/textValidatorCheckor", methods=['GET', 'POST'])
def text_validator_checkor():
    return render_template('textValidatorCheckor.html')


if __name__ == '__main__':
    app.run(port=8000)
