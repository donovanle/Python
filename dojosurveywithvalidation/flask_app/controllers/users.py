from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html', survey = User.showuser())

@app.route("/saveuser", methods=["POST"])
def saveuser():
    if User.is_valid(request.form):
        User.createuser(request.form)
        return redirect("/results")
    return redirect('/')
