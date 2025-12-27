import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # error ho to exception

    joke = response.json()

    print("😂 Joke of the Moment:")
    print(joke["setup"])
    print(joke["punchline"])

except requests.exceptions.RequestException as e:
    print("❌ API se data nahi aa paya")
    print("Error:", e)
