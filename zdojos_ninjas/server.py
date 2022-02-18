from flask import render_template,redirect,request,session,Flask
from dojo import Dojo, Ninja
app = Flask(__name__)

@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template("dojos.html" , all_dojos=dojos)

@app.route("/savedojo", methods=["POST"])
def savedojo():
    Dojo.createdojo(request.form)
    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def showdojo(dojo_id):
    data = { "id": dojo_id}
    return render_template("allninjas.html" , ninjas=Ninja.get_one_dojo(data))

@app.route('/ninja')
def showninjna_form():
    dojos = Dojo.get_all_dojos()
    return render_template("newninja.html" , all_dojos=dojos)

@app.route("/saveninja", methods=["POST"])
def saveninja():
    Ninja.createninja(request.form)
    return redirect("/dojos")

if __name__ == "__main__":
    app.run(debug=True)

