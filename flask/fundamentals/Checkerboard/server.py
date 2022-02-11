from flask import Flask,render_template
app = Flask(__name__)
@app.route('/<int:rows>/<int:columns>')
def checkers(rows, columns):
    return render_template('index.html' ,rows=rows, columns=columns )



@app.route('/')
def main_board():
    return render_template('index.html' ,rows=8, columns=8 )

@app.route('/<int:rows>')
def second_board(rows):
    return render_template('index.html' ,rows=rows, columns=8 )



if __name__=="__main__":
    app.run(debug=True)
 
