#!/usr/local/bin/python
# SERVER = Bedienen von Anfragen
import flask    # debug server, use tornado for live, später auch Django
app = flask.Flask(__name__)

# Idee: jeder schreibt seine eigene Funktion die man aufrufen kann
# dann git commit und push
# eventuell auf eigenem REchner testen (Programm starten und im Browser aufrufen)
# ich übernehme dann die Funktionen auf meinem Server
@app.route('/hallo')
def hallo():
	return "hallo"+str(3*3)

@app.route('/weekend')
def weekend_param():
	return "Bald ist Wochenende!!"

if __name__ == '__main__':
	print("Running on http://0.0.0.0:8080")
	app.run(debug=True, host='0.0.0.0', port=8080) # 80
