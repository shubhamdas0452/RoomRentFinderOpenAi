from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample PG data
pgs = [
    {
        "name": "Sunrise PG",
        "rent": 7500,
        "room": "single",
        "food": True,
        "wifi": True,
        "distance": 2.1
    },
    {
        "name": "Green Residency",
        "rent": 8000,
        "room": "single",
        "food": True,
        "wifi": True,
        "distance": 3.2
    },
    {
        "name": "City Homes",
        "rent": 6500,
        "room": "single",
        "food": False,
        "wifi": True,
        "distance": 4.5
    },
    {
        "name": "Comfort Stay",
        "rent": 6000,
        "room": "double",
        "food": True,
        "wifi": True,
        "distance": 3.8
    },
    {
        "name": "Waterside Stay",
        "rent": 9000,
        "room": "double",
        "food": True,
        "wifi": True,
        "distance": 5.8
    }
]


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# PG search API
@app.route("/api/search", methods=["POST"])
def search_pg():

    data = request.get_json()

    budget = data.get("budget", 8000)
    room = data.get("room", "single")
    food = data.get("food", False)
    wifi = data.get("wifi", False)

    results = []

    for pg in pgs:

        # Check budget
        if pg["rent"] > budget:
            continue

        # Check room type
        if pg["room"] != room:
            continue

        # Check food
        if food and not pg["food"]:
            continue

        # Check Wi-Fi
        if wifi and not pg["wifi"]:
            continue

        results.append(pg)

    return jsonify(results)


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)