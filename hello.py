
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from search import *

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Search:', validators=[validators.required()])

@app.route("/", methods=['GET', 'POST'])
def hello():
    result = None

    form = ReusableForm(request.form)   #for is the users search
    #print(form)
    #print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        #print (name)  #prints users search to the console
        result = searchPerson(name)
        
        if result == None:
            result = 'try again'

    return render_template('hello.html', form=form, final = result)

@app.route("/results", methods=['GET', 'POST'])
def results():
    return render_template('main.html')


#@app.route('/page_info/<id>')
#def page_info(id):
#    for name in image_info: #checking the id to find the right key in the dictionary to get the right id, title, and flickr_user
#        if name['id_1'] == id:
#            id_1 = name['id_1']
#            title = name['title']
#            flickr_user = name['flickr_user']


#    return render_template("page_info.html", picId_1 = id_1, title_1 = title, flickr_user_1 = flickr_user)



if __name__ == "__main__":
    app.run()
