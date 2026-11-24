import json

response = """{
  "companies": [
    {"corporate_number": "0000000000001", "name": "A社", "address": "東京都"},
    {"corporate_number": "0000000000002", "name": "B社", "address": "大阪府"}
  ]
}"""
def parse_companies(response_text):
    parsed = json.loads(response_text)
    company_list = parsed["companies"]
    return company_list

print(parse_companies(response))
