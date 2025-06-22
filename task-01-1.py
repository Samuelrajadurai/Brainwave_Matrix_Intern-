import tldextract
import re

phishing_domains = [
    "revil.ru", "conti.ru", "nso.il", "doubledragon.cn",
    "ryul.ru", "spam.com", "examplephish.com", "malicious.site"
]

safe_domains = [
    "google.com", "youtube.com", "wikipedia.org", "github.com"
]

suspicious_tlds = ['.tk', '.xyz', '.zip', '.cn']

url = input("Enter a URL: ").strip().lower()

# Extract domain
extracted = tldextract.extract(url)
domain = f"{extracted.domain}.{extracted.suffix}"

# Check against lists
if domain in phishing_domains:
    print("This URL is a PHISHING site. Do NOT trust it!")
elif domain in safe_domains:
    print("This URL is SAFE and trusted.")
else:
    if any(domain.endswith(tld) for tld in suspicious_tlds):
        print("Suspicious TLD detected. Be cautious.")
    elif re.match(r"\d{1,3}(\.\d{1,3}){3}", domain):
        print("IP address used in URL. Might be risky.")
    else:
        print("This URL is NOT in our database. Proceed with caution.")
