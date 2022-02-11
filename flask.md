# Flask Cheat Sheet

---
## flask
-setting up flask new file
1. make new folder
1. install flask to file
    - 'pipenv install flask'
    - 'pipenv shell'
1. - from flask import Flask,render_template
     app = Flask(__name__)
     @app.route('/')
     def checkers():
     return render_template('index.html')



        if __name__=="__main__":
        app.run(debug=True)


