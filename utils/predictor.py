import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_failure(temp, vib, pres, hours):
    data = np.array([[temp, vib, pres, hours]])
    result = model.predict(data)[0]

    reason = ""
    if vib > 0.7:
        reason += "High Vibration detected. "
    if temp > 50:
        reason += "High Temperature detected. "
    if hours > 400:
        reason += "Machine overused. "

    if result == 1:
        status = "⚠️ High Risk of Failure"
        alert = "🚨 ALERT: Immediate Maintenance Required!"
    else:
        status = "✅ Machine is Safe"
        alert = ""

    return status, reason, alert