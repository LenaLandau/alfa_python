#!/usr/local/bin/python
# SERVER = Bedienen von Anfragen
import flask    # debug server, use tornado for live, später auch Django
app = flask.Flask(__name__)

@app.route('/hallowelt')
def hello_param():
	return str(42)

if __name__ == '__main__':
	print("Running on http://0.0.0.0:8080")
	app.run(debug=True, host='0.0.0.0', port=8080) # 80
