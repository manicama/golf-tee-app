```markdown
# ⛳ Golf Tee Time Aggregator

A web application that compares golf tee times across multiple booking sources so golfers can find the best available times in one place.

Built by Michael Anicama as a hands-on project to learn Python, Flask, and APIs.

---

## 🚀 What It Does

- Displays available tee times from multiple sources (GolfNow, Lincoln Park direct)
- Shows live weather conditions at the course using the Open-Meteo API
- Allows filtering tee times by source
- Built with a clean separation between data, backend logic, and frontend display

---

## 🛠️ Technologies Used

- **Python** — core programming language
- **Flask** — lightweight web framework for serving pages
- **Jinja2** — templating language for dynamic HTML
- **HTML/CSS** — frontend structure and styling
- **Requests** — Python library for making API calls
- **Open-Meteo API** — free weather API (no key required)

---

## 📁 Project Structure

```
golf-tee-app/
├── app.py          # Main Flask application, routes and logic
├── data.py         # Data layer — mock tee times and API calls
├── static/
│   └── style.css   # Stylesheet
├── templates/
│   └── index.html  # Frontend template
└── README.md       # You are here
