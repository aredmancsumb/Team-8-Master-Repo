
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from search import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

class ReusableForm(Form):
    name = TextField('Search:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def home():

    form = ReusableForm(request.form)   #for is the users search
    if request.method == 'POST':
        name=request.form['name']

    return render_template('home.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():

    form = ReusableForm(request.form)   #form is the users search
    if request.method == 'POST':
        name=request.form['name']
        result = defineApi(name)
        filter(name, ['people', 'persons', 'characters', 'planets', 'starships', 'species', 'vehicles'])
        extra_info = f'This page does not show all results for {repr(name)}. Please try a name to get a more detailed response.'
        if result == '':
            extra_info = 'Try again'
    return render_template('results.html', form=form, final=result, user_search=name, extra_info=extra_info)



if __name__ == "__main__":
    app.run()
