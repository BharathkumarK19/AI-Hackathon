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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
