crypto_live_bot.py

import requests

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano",
        "order": "market_cap_desc"
    }
    response = requests.get(url, params=params)
    return response.json()

def recommend_live_crypto(user_query):
    user_query = user_query.lower()
    data = fetch_crypto_data()

    if "price" in user_query:
        return "\n".join([f"{coin['name']}: ${coin['current_price']}" for coin in data])

    elif "trending" in user_query or "rising" in user_query:
        rising = [coin['name'] for coin in data if coin['price_change_percentage_24h'] > 0]
        return f"Trending up: {', '.join(rising)} 📈"

    elif "market cap" in user_query:
        return "\n".join([f"{coin['name']}: Market Cap ${coin['market_cap']:,}" for coin in data])

    else:
        return "Ask about price, market cap, or what's trending."

print("⚠️ Crypto is risky—DYOR!")
print("Welcome to CryptoBuddy Live 💬 (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("CryptoBuddy:", recommend_live_crypto(user_input))

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def extract_intent(user_query):
    tokens = word_tokenize(user_query.lower())
    if "eco" in tokens or "sustainable" in tokens or "green" in tokens:
        return "sustainability"
    elif "price" in tokens:
        return "price"
    elif "trend" in tokens or "trending" in tokens or "rising" in tokens:
        return "trending"
    elif "cap" in tokens:
        return "market cap"
    else:
        return "unknown"

intent = extract_intent(user_input)
print("CryptoBuddy:", recommend_live_crypto(intent))
