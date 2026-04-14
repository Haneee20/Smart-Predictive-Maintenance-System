from flask import Flask, render_template, request
from utils.predictor import predict_failure
import matplotlib.pyplot as plt
import os
import json

app = Flask(__name__)

# 🔹 Load history from file
def load_history():
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            return json.load(f)
    return []

# 🔹 Save history to file
def save_history(data):
    with open("history.json", "w") as f:
        json.dump(data, f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reason = None
    alert = None
    graph_path = None
    probability = 0
    solution = None

    # 👉 Load previous history
    history = load_history()

    if request.method == "POST":
        temp = float(request.form["temperature"])
        vib = float(request.form["vibration"])
        pres = float(request.form["pressure"])
        hours = float(request.form["usage"])

        result, reason, alert, probability, solution = predict_failure(temp, vib, pres, hours)

        # 👉 Add new entry
        history.append({
            "temp": temp,
            "vib": vib,
            "pres": pres,
            "hours": hours,
            "result": result
        })

        # 👉 Save updated history
        save_history(history)

        # Graph
        values = [temp, vib, pres, hours]
        labels = ["Temperature", "Vibration", "Pressure", "Usage"]

        plt.figure()
        plt.bar(labels, values)
        plt.title("Sensor Data")

        graph_path = "static/graph.png"
        plt.savefig(graph_path)
        plt.close()

    return render_template("index.html",
                           result=result,
                           reason=reason,
                           alert=alert,
                           graph=graph_path,
                           probability=probability,
                           solution=solution,
                           history=history)

if __name__ == "__main__":
    app.run(debug=False)