def predict_failure(temp, vib, pres, hours):
    score = (temp * 0.3 + vib * 20 + pres * 15 + hours * 0.01)

    probability = min(score, 100)

    if probability > 70:
        result = "⚠️ High Risk of Failure"
        alert = "🚨 Immediate Maintenance Required!"
    elif probability > 40:
        result = "⚠️ Moderate Risk"
        alert = "⚠️ Check machine condition"
    else:
        result = "✅ Machine is Safe"
        alert = None

    # Reason
    reason = []
    if temp > 80:
        reason.append("High Temperature")
    if vib > 1:
        reason.append("High Vibration")
    if pres > 2:
        reason.append("High Pressure")
    if hours > 500:
        reason.append("Over Usage")

    reason = ", ".join(reason) if reason else "All parameters normal"

    # Solution
    if "Temperature" in reason:
        solution = "Cool down machine"
    elif "Vibration" in reason:
        solution = "Check alignment"
    elif "Pressure" in reason:
        solution = "Inspect pressure system"
    else:
        solution = "No action needed"

    return result, reason, alert, probability, solution