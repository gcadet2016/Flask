from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def routeLogin():
	if request.method == 'POST':
		print(request.form['mail'])
		print('C\'est un POST')
	else:
		print('C\'est un GET')
	return render_template('index.html')

app.debug = True
app.run()