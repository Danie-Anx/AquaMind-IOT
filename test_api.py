import requests

# URL do seu endpoint Flask
url = "http://localhost:5000/predict"

payload = {
    "temperature": 28.4,
    "hour":        15,
    "dayofyear":   145,
    "roll_moist":  32.1
}

resp = requests.post(url, json=payload)
print("Status code:", resp.status_code)
print("Resposta JSON:", resp.json())
