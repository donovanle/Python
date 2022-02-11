from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/') 
def index_one():
    if 'count' in session:
        print('key exists!')
    else:
        print('count key created')
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/count')
def count_page():
    session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session') 
def index_two():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    

# known problem: if /destroy_session is used with session['count'] += 1 shows error but with if else statemnt it declares the variable.

# create two buttons one for click and one for reset

# Want click button to redirect to '/count' and add 1 to session['count']

# Want restet button to redirect to '/destroy_session'