from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!"


@app.route('/about')
def about():
    return """< h1 > Hello we are the devs < /h1 >
    <p > We are using flask to make webb-apps < /p >"""


@app.route('/monday')
def monday():
    return render_template('monday.html', title="Monday")


@app.route('/tuesday')
def tuesday():
    return render_template('tuesday.html',
                           title="Tuesday", one="bubble gum", two="gum")


@app.route('/wednesday')
def wednesday():
    return render_template('wednesday.html', banana="I've got balls of steel!")

@app.route('/thursday')
def thursday():
    weekdays = ["monday", "tuesday", "wednesday",
                "thurday", "friday", "saturday", "sunday"]
    return render_template('thursday.html', week_days=weekdays)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
