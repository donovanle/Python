from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html" ,all_users=users)

@app.route("/users/new")
def new_user():
    return render_template("index_two.html")

@app.route("/save_user", methods=["POST"])
def save_user():
    User.create(request.form)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)

