import random
from flask import Flask,render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "My very secret key"


@app.route('/')
def index_one():
    session['rannum'] = int(random.randint(1,100))
    session['guess']= 0 
    print(session['rannum'])
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess_page():
    session['guess']= int(request.form['numguess'])
    print(request.form)
    print(session['rannum'])
    print(session['guess'])
    return render_template('index.html')

@app.route('/destroy_session') 
def index_two():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
