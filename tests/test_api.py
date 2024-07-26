import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Test NER API")
parser.add_argument('text', type=str, help='Text to analyze for named entities')
args = parser.parse_args()

url = "http://localhost:8000/predict/"

input_text = {
    "text": args.text
}

response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps(input_text))

if response.status_code == 200:
    result = response.json()
    print(result)
    print()
    print("Entities and their tags:\n")
    for entity in result["entities"]:
        print(f"Token: {entity[0]}, Tag: {entity[1]}")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
