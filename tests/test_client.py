import requests

response = requests.post(
    "http://127.0.0.1:5000/ask_guru",
    json={"question": "Explain karma from the Gita"}
)

print("Response from Sloka Guru:\n", response.json())
