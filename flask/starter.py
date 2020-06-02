from flask import Flask,request,make_response,redirect,url_for

app = Flask(__name__)



fruit = {'apple':'red','banana':'yellow','cranberry':'crimson','date':'brown'}

@app.route('/fruits/')
def fruit_list():
	fruit_str = "<br />".join(["A {} is {}".format(*i) for i in fruit.items()])
	form_str = """<br>Add something:
			<form method="post">
			<input type ="text" name="fruit_name"></input>
			<input type ="text" name="fruit_color"></input>
				"""
	header_str = """<html><head><title>TEST</title></head><body>"""
	footer_str = """</body></html>"""
	return header_str +fruit_str+form_str+footer_str

@app.route('/fruits/<name>/')
def single_fruit(name):
	if name in fruit.keys():
		return "A {} is {}".format(name,fruit[name])
	else:
		return make_response("ERROR: FRUIT NOT FOUND",404)

@app.route('/fruits/',methods=['POST'])
def add_fruit():
	print(request.form)
	print(request.data)
	fruit[request.form['fruit_name']] = request.form['fruit_color']

app.run(host='0.0.0.0',port=8999)