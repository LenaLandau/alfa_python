# SERVER = Bedienen von Anfragen
import flask    # debug server, use tornado for live, später auch Django
app = flask.Flask(__name__)

# ERREICHBAR UNTER http://alfa.pannous.com/hallo …

# Idee: jeder schreibt seine eigene Funktion die man aufrufen kann
# dann git commit und push
# eventuell auf eigenem Rechner testen (Programm starten und im Browser aufrufen)
# ich übernehme dann die Funktionen auf meinem Server
@app.route('/hallo')
def hallo():
	return "hallo "+str(41+1)

@app.route('/weekend')
def weekend_param():
	return "Bald ist Wochenende!!"

@app.route('/TGIF')
def Idea():
	return "Wir sollen am WE feiern gehen"


@app.route("/python")
def python_kurs():
	return "Wir lernen Python"

@app.route('/newtryJ')
def floor_function(): # fixed by K. ;)
	if 'value' in flask.request.args:
		value = int(flask.request.args['value'])
	else:
		return "MISSING param 'value'\n"
	if value < 0:
		return int(value) - 1
	else:
		return int(value)
	
@app.route("/wetter")
def wetter():
	return "Es ist sonnig."


if __name__ == '__main__':
	print("Running on http://0.0.0.0:8080")
	app.run(debug=True, host='0.0.0.0', port=8080) # 80
