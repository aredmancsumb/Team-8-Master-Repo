'''
Course: CST 205
Title: hello.py
Abstract: This file renders our html templates, and passes information we need in the html templates.
Authors: Maud Werkman, Ricardo Baca, Alexander Redman
Date: 5-14-2018
Github: https://github.com/aredmancsumb/Team-8-Master-Repo
'''

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from search import *

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

class ReusableForm(Form):   #This the function that gets what the user typed into the search bar and stores into a variable
    name = TextField('Search:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello(): # the function that renders our first HTML page and asks the user to enter in a search

    form = ReusableForm(request.form)

    return render_template('hello.html', form=form)

@app.route("/results", methods=['GET', 'POST'])
def results():
    result = []
    extra_info = ''
    name = ''
    form = ReusableForm(request.form)   #form gets the from from hello.html
    if request.method == 'POST':
        name = request.form['name']     #here we get the input from the user that's typed into the search bar
        result = defineApi(name)        #here we do the defineApi function from search.py which returns the results that go with the user input
        if name != '' and result != []:
            full_name = result[0][0][1][1]      #Navigates to the correct spot in the list saves the exact name from the results of defineApi to a new variable "full_name"
    if name == '':
        extra_info = 'Please enter a valid search term.'  #if the user doesn't enter a search term, they get this message
        full_name = 'Try Again'
    if result == []:
        extra_info = 'Please try again. For a detailed result, try searching for a name.'  #if there are no results found for the search term, you get this message
        full_name = 'Try Again'
    return render_template('main.html', form=form, final=result, user_search=name, extra_info=extra_info, full_name=full_name)      #passes all neccesary variables to the results page "main.html"
if __name__ == "__main__":
    app.run()
