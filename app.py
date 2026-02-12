from flask import Flask, jsonify
import requests
from typing import List

app = Flask(__name__)

# MODEL CLASSES
class Company:
    def __init__(self, id, name, address, zip_code, country,
                 employee_count, industry, market_cap, domain, logo):
        self.id = id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.country = country
        self.employee_count = employee_count
        self.industry = industry
        self.market_cap = market_cap
        self.domain = domain
        self.logo = logo

    def to_dict(self):
        return self.__dict__


class CompanyResponse:
    def __init__(self):
        self.companies: List[Company] = []
        
    def add_company(self, company: Company):
        self.companies.append(company)

    def to_dict(self):
        return {
            "companies": [c.to_dict() for c in self.companies]
        }
    
URL = "https://fake-json-api.mock.beeceptor.com/companies"
def fetch_companies() -> CompanyResponse:
    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception("Failed to fetch data")

    data = response.json()
    result = CompanyResponse()

    for item in data:
        company = Company(
            id=item.get("id"),
            name=item.get("name"),
            address=item.get("address"),
            zip_code=item.get("zip"),
            country=item.get("country"),
            employee_count=item.get("employeeCount"),
            industry=item.get("industry"),
            market_cap=item.get("marketCap"),
            domain=item.get("domain"),
            logo=item.get("logo")
        )
        print(company.__dict__)
        result.add_company(company)

    return result


# API ENDPOINT  
@app.route("/companies", methods=["GET"])
def get_companies():
    result = fetch_companies()
    return result.to_dict()

# RUN SERVER
if __name__ == "__main__":
    app.run(debug=True)
