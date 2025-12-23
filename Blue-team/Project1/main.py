import json
from parser.linux_parser import parse_auth_log
from detections.brute_force import detect_bruteforce

LOG_FILE = "logs/auth.log"
OUTPUT_FILE = "output/alerts.json"

def main():
    print("[] Parsing logs...")
    events = parse_auth_log(LOG_FILE)

    print(f"[] {len(events)} events collected")

    print("[*] Running detections...")
    alerts = detect_bruteforce(events)

    print(f"[!] {len(alerts)} alerts generated")

    with open(OUTPUT_FILE, "w") as f:
        json.dump(alerts, f, indent=4)

    print(f"[+] Alerts saved to {OUTPUT_FILE}")

if name == "main":
    main()