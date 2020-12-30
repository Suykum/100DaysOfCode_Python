from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

GENDERIZE_endpoint = "https://api.genderize.io?name=peter"
AGIFY_ENDPOINT = "https://api.agify.io?name=michael"


@app.route('/')
def hello_world():
    random_number = random.randint(0, 10)
    year = datetime.datetime.today().year
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def genderize_agify(name):
    parameters = {"name": name}
    gender_result = requests.get(url=GENDERIZE_endpoint, json=parameters).json()
    gender = gender_result["gender"]
    age_result = requests.get(url=AGIFY_ENDPOINT, json=parameters).json()
    age = age_result["age"]
    return render_template("gender_age.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
