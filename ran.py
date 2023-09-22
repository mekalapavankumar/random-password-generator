
from flask import Flask,render_template
import requests

app = Flask(__name__)
app.static_folder = 'static'

key = "9b1c23273e5f762602f0b20d1ef951c4"
url = "http://data.fixer.io/api/latest?access_key=" + key

@app.route('/',methods = ['POST','GET'])

def hello_world():
	return render_template("ran.html")



if __name__ == '__main__':
	app.run(debug = True)
