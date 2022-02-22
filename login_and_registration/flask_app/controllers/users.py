from flask_app import app
from flask import render_template,redirect,request,flash, session
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def saveuser():
    if not User.email_is_valid(request.form):
        return redirect('/')
    if not User.validate_user(request.form):
        return redirect('/')
    User.createuser(request.form)
    return redirect("/")


@app.route('/login', methods=["POST"])
def login():
    if User.validate_login(request.form):
        data = {
        "email": request.form['email']
        }
        user = User.user_email(data)
        session['user_id'] = user.id
        return redirect('/success')
    else:
        return redirect('/')

@app.route("/success")
def loggedin():
    data = {
        "id": session['user_id']
    }
    user = User.user_id(data)
    return render_template("success.html",user=user)


@app.route('/logout') 
def index_two():
    session.clear()
    return redirect('/')