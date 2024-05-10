#!/usr/local/bin/python
import flask # debug server, use tornado for live
app = flask.Flask(__name__)


@app.route('/')
def show_endpoints():
	return "ENDPOINTS: "+str(app.url_map)

# @app.route('/index')
# def index():
# 	return flask.render_template('index.html', has_result=False)

@app.route('/hello')
def hello_param():
	if 'query' in flask.request.args:
		query = flask.request.args['query']
	else:
		return "MISSING param 'query'\n"
	return query*2


@app.route('/newtryJ')
def floor_function(value,float)->int:
	if value < 0:
		return int(value) - 1
	else:
		return int(value)
	
	

if __name__ == '__main__':
	print("Running on http://0.0.0.0:5000")
	app.run(debug=True, host='0.0.0.0', port=5000)
