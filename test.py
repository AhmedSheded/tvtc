# import requests
#
# def make_request(question):
#     url = "http://127.0.0.1:8000/ai"
#     data = {'question': question}
#     response = requests.post(url, data=data)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": "Failed to get a response from the API."}
#
# # Example usage:
# question = "انا مستجد ولم يصلني الرقم التدريبي"
# response = make_request(question)
# print(response)

import requests
import json

# URL of your Django server
url = 'http://127.0.0.1:8000/ai'  # Replace with your actual API endpoint

# Data to be sent in the POST request
data = {
    'question': 'أنا مستجد ولم يصلني الرقم التدريبي'
}

# Convert data to JSON format
json_data = json.dumps(data)

# Send POST request to the Django server
response = requests.post(url, json=json_data)

# Print the response
print(response.json())
