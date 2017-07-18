from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'randomnumber'

@app.route('/')
def index():
    session['number'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['action'] == 'reset':
        session.pop('number')
        return redirect('/')
    else:
        session['guess'] = int(request.form['guess'])
        if session['guess'] > session['number']:
            return render_template('high.html')
        elif session['guess'] < session['number']:
            return render_template('low.html')
        else:
            return render_template('correct.html')

app.run(debug=True)
