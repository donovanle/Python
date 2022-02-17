from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/users")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html" ,all_users=users)

@app.route("/users/<int:user_id>")
def show_user(user_id):
    data = { "id": user_id}
    return render_template("index_show.html" ,user=User.get_one(data))

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    data = { "id": user_id}
    return render_template("index_edit.html", user=User.get_one(data))

@app.route("/users/new")
def new_user():
    return render_template("index_two.html")

@app.route("/save_user", methods=["POST"])
def save_user():
    User.create(request.form)
    return redirect("/users")

@app.route("/update_user", methods=["POST"])
def update_user():
    User.update(request.form)
    return redirect("/users")

@app.route("/users/<int:user_id>/destroy")
def delete_user(user_id):
    data = { "id": user_id}
    User.delete(data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)

