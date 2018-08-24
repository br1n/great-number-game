from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "henlo"


@app.route('/')
def index():
    if "correct" not in session:
        session["correct"] = random.randint(1,101)
    if "result" not in session:
        result = "no guess"
    else:
        result = session["result"]
    return render_template('index.html', result=result)

@app.route("/guess", methods=['POST'])
def guess():
    guess = int(request.form["guess"])
    correct = session["correct"]
    if guess > correct:
        session["result"] = "high"
    elif guess < correct:
        session["result"] = "low"
    else:
        session["result"] = "correct"
    return redirect('/')

@app.route('/reset')
def reset():
    session['correct']
    session.pop('correct')
    session.pop("result")
    return redirect('/')

app.run(debug=True)
