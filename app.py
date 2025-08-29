from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined domains and problems
domains = {
    "AI": ["Build a chatbot", "Image classification", "Recommendation system"],
    "Web Development": ["Create a job portal", "E-commerce website", "Portfolio builder"],
    "Cybersecurity": ["Detect phishing emails", "Secure login system"],
    "Data Science": ["Student performance prediction", "Crop yield forecasting"]
}

@app.route("/", methods=["GET", "POST"])
def home():
    selected_domain = None
    problems = []

    if request.method == "POST":
        selected_domain = request.form.get("domain")
        problems = domains.get(selected_domain, [])

    return render_template(
        "index.html",
        domains=domains.keys(),
        selected_domain=selected_domain,
        problems=problems
    )

if __name__ == "__main__":
    # ✅ This keeps Flask running until you stop it (CTRL+C)
    app.run(debug=True, port=5000)
