from flask import Flask, request, jsonify

app = Flask(__name__)
temp = 15

def loadTemp():
    return temp

def writeTemp(newTemp):
    temp = newTemp

@app.route("/gettemp", methods=['GET'])
def getTemp():
    temp = loadTemp()
    return "<p>Temperatur: " + str(temp) + "°C</p>"

@app.route("/gettempapi", methods=['GET'])
def getTempApi():
    temp = loadTemp()
    raw_data = {"temp":temp}
    return jsonify(raw_data)

@app.route("/settemp", methods=['POST'])
def setTemp():
    global temp
    data = request.get_json()
    temp = data['temp']
    print(temp)

    return jsonify(True)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)