# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (díficil y sin dependencias)
import urllib.request
import json

DEEPSEEK_API_KEY = "sk-8b9a56ebeab0496d953f7b911e61afdf"

api_posts = "https://jsonplaceholder.typicode.com/posts/"
try:
  response = urllib.request.urlopen(api_posts)
  data = response.read()
  js_data = json.loads(data.decode("utf-8"))
  print(js_data)
  response.close()
except urllib.error.URLError as e:
  print("Error en la petición:", e) 
  

# 2. Con dependencias (request)
import requests

print("\nGET")
api_posts = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(api_posts)
if response.status_code == 200:
    js_data = response.json()
json_response = response.json()
print(json_response)

# 3. un POST con request
print("\nPOST")
try:
    api_post = "https://jsonplaceholder.typicode.com/posts/"
    post_data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    } 
    response = requests.post(api_post, json=post_data)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)

# 4. PUT
print("\nPUT")
try:
    api_post = "https://jsonplaceholder.typicode.com/posts/1"
    put_data = {
        "id": 1,
        "title": "foo",
        "body": "bar",
        "userId": 1
    } 
    response = requests.put(api_post, json=put_data)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)
    
# usar la API de chat GPT o openAI

OPENEAI_KEY = "sk-XXXXXXX"
url = "https://api.openai.com/v1/chat/completions"
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {OPENEAI_KEY}"
}
prompt = "Escribe un breve poema sobre la primavera"
data = {
  "model":"gpt-4o-mini",
  "messages":[
    {"role":"user","content": prompt}
  ]
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)

call_openai_gpt = (OPENEAI_KEY, "Escribe un breve poema sobre la primavera")

print(json.dumps(response.json(), indent=2))

# llamar a la API de DeepSeek

import json

def call_deepseek(api_key, prompt):
    url = "https://api.deepseek.ai/v1/chat/completions"
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }
    data = {
      "model": "deepseek-chat",
      "messages": [
        {"role": "user", "content": prompt}
      ]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
response = call_deepseek(DEEPSEEK_API_KEY, "Escribe un breve poema sobre la primavera")
print(response.json())


# print(json.dumps(response, indent=2))
print(response["choices"][0]["message"]["content"]) 