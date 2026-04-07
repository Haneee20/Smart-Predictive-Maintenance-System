from flask import Flask, render_template, request
from utils.predictor import predict_failure
import matplotlib.pyplot as plt
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    reason = None
    alert = None
    graph_path = None

    # 🔥 Auto-generate sensor data
    auto_temp = round(random.uniform(30, 70), 2)
    auto_vib = round(random.uniform(0.2, 1.0), 2)
    auto_pres = round(random.uniform(1.0, 2.0), 2)
    auto_hours = round(random.uniform(100, 600), 2)

    # 🔥 Auto prediction (real-time simulation)
    result, reason, alert = predict_failure(auto_temp, auto_vib, auto_pres, auto_hours)

    # 🔥 Create graph
    values = [auto_temp, auto_vib, auto_pres, auto_hours]
    labels = ["Temp", "Vibration", "Pressure", "Usage"]

    plt.figure()
    plt.plot(labels, values, marker='o')
    plt.title("Sensor Data Visualization")

    graph_path = "static/graph.png"
    plt.savefig(graph_path)
    plt.close()

    return render_template(
        "index.html",
        result=result,
        reason=reason,
        alert=alert,
        graph=graph_path,
        auto_temp=auto_temp,
        auto_vib=auto_vib,
        auto_pres=auto_pres,
        auto_hours=auto_hours
    )

if __name__ == "__main__":
    app.run(debug=True)