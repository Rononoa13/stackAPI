import requests
import json
import urls


stack_all_answers = urls.API_URL['answers']
# print(stack_all_answers)

response = requests.get(stack_all_answers)
print(response.status_code)
data = response.json()
print(json.dumps(response.json(), indent=3))