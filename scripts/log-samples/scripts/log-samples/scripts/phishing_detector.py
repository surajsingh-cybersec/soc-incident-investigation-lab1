phishing_keywords = ["urgent", "verify", "click", "password", "account"]

email_file = "log-samples/email-log.txt"

with open(email_file, "r") as file:
    content = file.read().lower()

print("Detected Phishing Indicators:")
for word in phishing_keywords:
    if word in content:
        print(f"Suspicious keyword found: {word}")
