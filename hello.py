from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from search import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Search:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():

    form = ReusableForm(request.form)   #for is the users search

    return render_template('hello.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():
    result = []
    extra_info = ''
    name = ''
    form = ReusableForm(request.form)   #form is the users search
    if request.method == 'POST':
        name = request.form['name']
        result = defineApi(name)
        if name != '' and result != []:
            full_name = result[0][0][1][1]
    if name == '':
        extra_info = 'Please enter a valid search term.'
        full_name = 'Try Again'
    if result == []:
        extra_info = 'Please try again. For a detailed result, try searching for a name.'
        full_name = 'Try Again'
    return render_template('main.html', form=form, final=result, user_search=name, extra_info=extra_info, full_name=full_name)
if __name__ == "__main__":
    app.run()
