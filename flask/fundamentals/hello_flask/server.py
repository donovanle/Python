from doctest import OutputChecker
from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hi(name):
    return f'Hi {name.capitalize()}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    words = ''
    for i in range(0,num):
        words += f"<p>{word}</p>"
    return words


if __name__=="__main__":   
    app.run(debug=True)    

