failed_attempts = {}

log_file = "log-samples/auth.log"

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split()[-4]
            failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

print("Potential Brute Force Sources:")
for ip, count in failed_attempts.items():
    if count >= 3:
        print(f"IP: {ip} | Failed Attempts: {count}")
