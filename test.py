import requests

msgs = [
    "What is machine learning?",
    "Explain Docker in simple terms",
    "What is the difference between REST and GraphQL?",
]*2

for m in msgs:
    print(requests.post(
        "https://onekey-8pr2.onrender.com/proxy/u/groq/cbhorg",
        headers={"Authorization":"Bearer apikey-groq-cbhorg","Content-Type":"application/json"},
        json={"model":"groq/compound-mini","messages":[{"role":"user","content":m}]}
    ).json())


