import os
from flask import Flask,render_template,request,make_response,redirect,url_for

templates = os.path.join(os.getcwd(),'templates')
app = Flask(__name__,template_folder=templates)

fruit = {'apple':'red','banana':'yellow','cranberry':'crimson','date':'brown'}


@app.route('/fruits/')
def fruit_list():
	return render_template('fruit_list.html',fruits=fruit)

@app.route('/fruits/<name>/')
def single_fruit(name):
	if name in fruit.keys():
		return render_template('single_fruit.html',name=name,color=fruit[name])
	else:
		return make_response("ERROR: FRUIT NOT FOUND",404)	