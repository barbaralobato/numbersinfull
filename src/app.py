from flask import Flask
from flask import jsonify
import utils

app = Flask(__name__)

@app.route("/<number>")
def get_number(number):
	try:
		written_number = utils.write_number(int(number))
		result = { "extenso" : written_number }
	except ValueError:
		result = { "error" : "route not found!" }

	return jsonify(result)

if __name__=="__main__":
	app.run(debug=True, host='0.0.0.0')