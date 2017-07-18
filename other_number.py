from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'SuperSecret'

#def sessRange():
    #session['range'] = random.randrange(0,101)

@app.route('/')
def great_numbers():
    session['number'] = random.randrange(0,101)
    return render_template('other_index.html')

@app.route('/guess', methods=['POST'])
def you_lost():


    print session

    randRange = int(request.form['num_value'])
    print randRange

    if session['guess'] > randRange:
        session['randRange'] = 'too low'
        print 'too low'

    elif session['guess'] < randRange:
        session['randRange'] = 'too high'
        print 'too high'

    else:
        session['randRange'] = 'you won'
        print 'you won'

    return redirect('/')

@app.route('/refresh')
def you_won():
    session.clear()
    return redirect('/')


app.run(debug=True)
