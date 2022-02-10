from doctest import OutputChecker
from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/play')          
def index_one():
    return render_template("index.html")

@app.route('/play/<int:num>')          
def index_two(num):
    return render_template("index.html", num=num)

@app.route('/play/<int:num>/<string:color>')
def index_three(num, color):
    return render_template("index.html", num=num, color=color)
if __name__=="__main__":   
    app.run(debug=True)    

