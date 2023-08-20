import json
import time
import requests
from bs4 import BeautifulSoup

def extract_results(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find("table", {"id": "listingTable"}).find_all("tbody")
    trow = table[0].find_all("tr")
    results = {}
    i = 1
    for cell in trow:
        if i <= 10:
            result_name = cell.find('td').text.strip()
            result_url = cell.find("a")["href"]
            results[result_name] = result_url
    return results

def save_results(results):
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)
        
def get_results():
    session = requests.Session()
    try:
        req = session.get("https://ktu.edu.in/eu/res/viewExamStudentResults.htm")
        soup = BeautifulSoup(req.content, "html.parser")
        crsf_token = soup.find("input", {"name": "CSRF_TOKEN"})["value"]
        req2 = session.post("https://ktu.edu.in/eu/res/viewExamStudentResults.htm", data={
            "CSRF_TOKEN": crsf_token,
            "form_name": "studentResultProgramForm",
            "programId": 1
        })
        return req2.content
    except Exception as e:
        print(e)
        return None

def load_results():
    try:
        with open("results.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def check_for_new_results():
    current_results = load_results()

    if page_content := get_results():
        new_results = extract_results(page_content)
        if added_results := {
            result: details
            for result, details in new_results.items()
            if result not in current_results
        }:
            save_results(current_results)
            return added_results
        else:
            return None
