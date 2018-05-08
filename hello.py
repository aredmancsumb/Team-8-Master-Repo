
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
    #print(form)
    #print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        #result = defineApi(name)
        #print (name)  #prints users search to the console

        #if result == None:
            #rusult = 'try again'

    return render_template('hello.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():
    result = None

    form = ReusableForm(request.form)   #form is the users search
    if request.method == 'POST':
        name=request.form['name']
        result = defineApi(name)
        #print (name)  #prints users search to the console
        #print(result)
        #defineApi(name)
        if result == None:
            result = ['try again']
    return render_template('main.html', form=form, final=result)


if __name__ == "__main__":
    app.run()
