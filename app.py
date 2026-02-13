from flask import Flask
import requests

app = Flask(__name__)

URL = "https://fake-json-api.mock.beeceptor.com/companies"
def fetch_companies():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
    return response.json()

# API ENDPOINT  
@app.route("/companies", methods=["GET"])
def get_companies():
    data = fetch_companies()
    return data

# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
