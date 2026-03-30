import requests

url = "https://cyber-threat-detection-3.onrender.com//predict"

data = {
    "features": [0]*41  # 41 features (important!)
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)