from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        device = int(request.form['device'])
        packet = int(request.form['packet'])
        protocol = int(request.form['protocol'])
        login = int(request.form['login'])
        location = int(request.form['location'])
        cpu = float(request.form['cpu'])

        features = np.array([[device, packet, protocol, login, location, cpu]])
        result = model.predict(features)[0]
        prediction = 'Threat Detected ⚠️' if result == 1 else 'Device is Safe ✅'

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)