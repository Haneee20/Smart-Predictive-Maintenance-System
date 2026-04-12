from flask import Flask, render_template, request
from utils.predictor import predict_failure
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reason = None
    alert = None
    graph_path = None

    if request.method == "POST":
        temp = float(request.form["temperature"])
        vib = float(request.form["vibration"])
        pres = float(request.form["pressure"])
        hours = float(request.form["usage"])

        result, reason, alert = predict_failure(temp, vib, pres, hours)

        # Graph
        values = [temp, vib, pres, hours]
        labels = ["Temperature", "Vibration", "Pressure", "Usage"]

        plt.figure()
        plt.plot(labels, values, marker='o')
        plt.title("Sensor Data")

        graph_path = "static/graph.png"
        plt.savefig(graph_path)
        plt.close()

    return render_template("index.html",
                           result=result,
                           reason=reason,
                           alert=alert,
                           graph=graph_path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)