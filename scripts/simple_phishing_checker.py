# scripts/simple_phishing_checker.py
# Simple Phishing URL Checker (Starter Version)
# Author: Ajmal Faiz

def is_phishing_url(url):
    """
    Very basic rules for phishing detection (demo version)
    """
    phishing_keywords = ["login", "verify", "update", "banking", "secure", "account"]
    suspicious = False

    # Rule 1: URL length > 75
    if len(url) > 75:
        suspicious = True

    # Rule 2: '@' symbol
    if "@" in url:
        suspicious = True

    # Rule 3: Suspicious keywords
    for word in phishing_keywords:
        if word in url.lower():
            suspicious = True

    return suspicious

# Demo test URLs
if __name__ == "__main__":
    test_urls = [
        "https://secure-login.bank-account-update.com",
        "https://www.google.com",
        "http://verify-your-account.com/login",
        "https://en.wikipedia.org/wiki/Phishing"
    ]

    for url in test_urls:
        print(f"{url} --> {'Phishing' if is_phishing_url(url) else 'Safe'}")
