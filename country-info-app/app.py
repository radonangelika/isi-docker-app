from flask import Flask, request, jsonify, render_template
import json
import os

port = int(os.environ.get("PORT", 5000))


app = Flask(__name__)

with open("countries.json") as f:
    countries = json.load(f)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/country")
def country():
    name = request.args.get("name")
    if not name:
        return render_template("index.html", error="Please provide a country name")

    results = [
        country for country in countries
        if name.lower() in country["name"].lower()
    ]

    if results:
        return render_template("countries.html", countries=results)
    else:
        return render_template("index.html", error=f"No match for '{name}'")


@app.route("/countries")
def countries_list():
    return render_template("countries.html", countries=countries)

@app.route("/currency")
def currency_filter():
    currency = request.args.get("currency")
    if not currency:
        return render_template("index.html", error="Provide currency code like EUR or PLN")
    
    results = [c for c in countries if c["currency"].lower() == currency.lower()]
    if results:
        return render_template("countries.html", countries=results)
    else:
        return render_template("index.html", error=f"No countries use currency '{currency}'")

@app.route("/add", methods=["GET", "POST"])
def add_country():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "capital": request.form["capital"],
            "population": int(request.form["population"]),
            "currency": request.form["currency"]
        }
        countries.append(data)

        # zapis do pliku JSON
        with open("countries.json", "w") as f:
            json.dump(countries, f, indent=2)

        return render_template("index.html", country=data)

    return render_template("add.html")
# ważne dla Dockera
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
