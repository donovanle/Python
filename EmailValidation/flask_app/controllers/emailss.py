from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.emails import Email

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('second.html', all_emails = Email.displayemails())

@app.route('/confirm', methods=["POST"])
def confirm():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.newemail(request.form)
    return redirect('/success')

@app.route('/remove/<int:id>')
def remove(id):
    data = {"id" : id}
    Email.deleteemail(data)
    return redirect('/success')


