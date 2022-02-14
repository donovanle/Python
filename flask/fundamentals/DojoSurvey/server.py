from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/') 
def index_one():
    return render_template('index.html')

@app.route('/results', methods=["POST"])
def results():
    print(request.form)
    session["name"]= request.form["full_name"]
    session["location"]= request.form["dojo_location"]
    session["language"]= request.form["fav_lan"]
    session["comment"]= request.form["commentss"]
    return render_template('secondary.html')

@app.route('/destroy_session') 
def index_two():
    session.clear()
    return redirect('/')



if __name__=="__main__":   
    app.run(debug=True)    
