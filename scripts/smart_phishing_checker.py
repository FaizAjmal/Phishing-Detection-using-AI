# scripts/smart_phishing_checker.py
# Author: Ajmal Faiz
# Enhanced Rule-Based Phishing URL Checker

import re

def is_phishing_url(url):
    """
    Enhanced rule-based phishing URL detection with scoring
    """
    phishing_keywords = ["login", "verify", "update", "banking", "secure", "account", "free", "payment"]
    score = 0

    # Rule 1: URL length
    if len(url) > 75:
        score += 1

    # Rule 2: '@' symbol
    if "@" in url:
        score += 1

    # Rule 3: Suspicious keywords
    for word in phishing_keywords:
        if word in url.lower():
            score += 1

    # Rule 4: IP address in URL
    ip_pattern = r"http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
    if re.match(ip_pattern, url):
        score += 1

    # Rule 5: HTTPS check
    if not url.startswith("https"):
        score += 0.5

    # Threshold: 2 or more points = phishing
    is_phishing = score >= 2

    return is_phishing, score

# Test URLs
if __name__ == "__main__":
    test_urls = [
        "https://secure-login.bank-account-update.com",
        "https://www.google.com",
        "http://verify-your-account.com/login",
        "https://192.168.1.1/login",
        "http://free-gift.com@malicious.com",
        "https://en.wikipedia.org/wiki/Phishing"
    ]

    for url in test_urls:
        phishing, score = is_phishing_url(url)
        status = "Phishing" if phishing else "Safe"
        print(f"{url} --> {status} (Score: {score})")
