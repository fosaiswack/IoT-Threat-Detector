# IoT-Threat-Detector
This project focuses on using artificial intelligence (AI) to detect cybersecurity threats in Internet of Things (IoT) environments

Here’s a professional and clear README.md file tailored specifically for your Flask app and project “Building AI Tools for Cybersecurity Threat Detection using Multimodal Data”.

You can copy and paste this into your GitHub repo’s README.md file:

⸻


# 🛡️ Building AI Tools for Cybersecurity Threat Detection using Multimodal Data

This project implements a machine learning model served through a Flask web app to detect cybersecurity threats in IoT devices. The model takes in multiple types of data (multimodal) such as device ID, network packet count, protocol type, login attempts, device location, and CPU usage — and classifies the device as either safe or under threat.

---

## 💡 Overview

Cybersecurity in IoT environments is increasingly critical due to the scale and sensitivity of data generated by smart devices. This project addresses the challenge by:

- Developing a supervised machine learning model for threat detection.
- Using **multimodal input features**: numerical and categorical inputs reflecting device and network behavior.
- Creating a simple, interactive **Flask-based frontend** for real-time predictions.

---

## 🧪 Input Features Used

| Feature      | Description                               |
|--------------|-------------------------------------------|
| `device`     | Encoded identifier for the device         |
| `packet`     | Number of packets sent/received           |
| `protocol`   | Protocol type used (e.g., TCP, UDP)       |
| `login`      | Count of login attempts                   |
| `location`   | Encoded physical or network location      |
| `cpu`        | Current CPU usage (%)                     |

---

## 🚀 How to Run the Project Locally

```bash
git clone https://github.com/fosaiswack/Iot-Threat-Detector
cd IoT-Threat-Detector
```p


2. Install Required Packages

Make sure you have Python installed, then install dependencies:

pip install -r requirements.txt

Include Flask, numpy, scikit-learn, and joblib in requirements.txt

3. Start the Flask App

python app.py

Then visit http://127.0.0.1:5000 in your browser.

⸻

🖥️ Flask App Code Explanation

The main file app.py performs the following:
	•	Loads a pre-trained ML model saved as model.pkl.
	•	Receives user inputs from a web form (in index.html).
	•	Makes a prediction based on inputs using the model.
	•	Returns a result back to the browser:
	•	✅ Device is Safe if classified as 0
	•	⚠️ Threat Detected if classified as 1

Example Prediction Flow:

features = np.array([[device, packet, protocol, login, location, cpu]])
result = model.predict(features)[0]


⸻

🧾 File Structure

├── model.pkl               # Pre-trained ML model
├── app.py                  # Flask backend logic
├── templates/
│   └── index.html          # HTML form interface
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation






