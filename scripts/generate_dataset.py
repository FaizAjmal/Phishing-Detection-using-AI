# scripts/generate_dataset.py
# Generates a small CSV dataset for ML experiments

import pandas as pd

# Sample URLs (you can extend later)
urls = [
    ("https://secure-login.bank-account-update.com", 1),
    ("https://www.google.com", 0),
    ("http://verify-your-account.com/login", 1),
    ("https://en.wikipedia.org/wiki/Phishing", 0),
    ("https://192.168.1.1/login", 1),
    ("http://free-gift.com@malicious.com", 1)
]

df = pd.DataFrame(urls, columns=["url", "label"])
df.to_csv("data/phishing_urls.csv", index=False)
print("Dataset saved to data/phishing_urls.csv")
