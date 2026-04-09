from flask import Flask, render_template, request
from data import get_tee_times, get_weather, get_forecast

app = Flask(__name__)

@app.route("/")
def home():
    source_filter = request.args.get("source", "")
    date_filter = request.args.get("date", "")
    course_filter = request.args.get("course", "")

    all_tee_times = get_tee_times()
    filtered = all_tee_times

    if course_filter:
        filtered = [
            t for t in filtered
            if course_filter.lower() in t["course"].lower()
        ]
    if source_filter:
        filtered = [
            t for t in filtered
            if source_filter.lower() in t["source"].lower()
        ]
    if date_filter:
        filtered = [
            t for t in filtered
            if t["date"] == date_filter
        ]

    next_available = None
    if date_filter and not filtered:
        future_dates = sorted([
            t["date"] for t in all_tee_times
            if t["date"] > date_filter
        ])
        if future_dates:
            next_available = future_dates[0]

    weather = get_weather()
    forecast = get_forecast()

    return render_template(
        "index.html",
        tee_times=filtered,
        current_filter=source_filter,
        current_date=date_filter,
        current_course=course_filter,
        weather=weather,
        forecast=forecast,
        next_available=next_available
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)