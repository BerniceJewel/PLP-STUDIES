crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
       },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

def recommend_crypto(user_query):
    user_query = user_query.lower()
    
    if "sustainable" in user_query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {best}! 🌱 (Sustainability: {crypto_db[best]['sustainability_score']}/10)"
    
    elif "trend" in user_query or "rising" in user_query:
        trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f"Trending coins: {', '.join(trending)} 📈"
    
    elif "profit" in user_query:
        profitable = [coin for coin in crypto_db 
                     if crypto_db[coin]["price_trend"] == "rising" 
                     and crypto_db[coin]["market_cap"] == "high"]
        return f"High-growth coins: {', '.join(profitable)} 💰"
    else:
        return "Ask about sustainability, price trends, or profits!"

# Test the bot
print(recommend_crypto("Which coin is most sustainable?"))
print(recommend_crypto("Which coin will give me profit?"))

print("⚠️ Crypto is risky—DYOR!")  # Show disclaimer on startup
print("👋 I'm CryptoBuddy. Ask me about crypto trends or sustainability!")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = recommend_crypto(user_input)
    print(f"CryptoBuddy: {response}")
