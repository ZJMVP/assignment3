from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zjmvp'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/showPie', methods=['GET', 'POST'])
def showPie():
    return render_template('ShowPie.html')


@app.route('/showBar', methods=['GET', 'POST'])
def showBar():
    return render_template('showBar.html')


@app.route('/showScatter', methods=['GET', 'POST'])
def showScatter():
    return render_template('showScatter.html')


if __name__ == '__main__':
    app.run(port=8000)
